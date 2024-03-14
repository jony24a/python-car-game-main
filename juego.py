import pygame
from pygame.locals import *
import random

from PlayerVehicle import PlayerVehicle
from Vehicle import Vehicle

pygame.init()


# Crear la ventana 
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Juego del Carrito By Jonatan Novoa')

# Colores
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# Tamaños de carreteras y marcadores
road_width = 300
marker_width = 10
marker_height = 50

# Coordenadas del carril
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# Marcadores de carreteras y bordes
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# Para animar el movimiento de los marcadores de carril
lane_marker_move_y = 0

# Coordenadas iniciales del jugador
player_x = 250
player_y = 400

# Ajustes de cuadro
clock = pygame.time.Clock()
fps = 120

# Configuración del juego
gameover = False
speed = 2
score = 0

               
# grupos de sprite
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# Crear el coche del jugador
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# Cargar las imágenes del vehículo
image_filenames = ['camioneta.png', 'trailer.png', 'taxi.png', 'van.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)
    
# Cargar la imagen de choque
crash = pygame.image.load('images/accidente.png')
crash_rect = crash.get_rect()

# Bucle de juego
running = True
while running:
    
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        # Mover el coche del jugador usando las teclas de flecha izquierda/ derecha
        if event.type == KEYDOWN:
            
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
                
            # Comprobar si hay una colisión de deslizamiento lateral después de cambiar de carril
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    
                    gameover = True
                    
                    # Colocar el coche del jugador al lado de otro vehículo
                    # Y determinar dónde colocar la imagen de choque
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
            
            
    # Dibujar el césped
    screen.fill(green)
    
    # Dibujar el camino
    pygame.draw.rect(screen, gray, road)
    
    # Dibujar los marcadores de borde
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)
    
    # Dibujar los marcadores de carril
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        
    # Dibujar el coche del jugador
    player_group.draw(screen)
    
    # Añadir un vehículo
    if len(vehicle_group) < 2:
        
        # Asegurar que haya suficiente espacio entre los vehículos
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
                
        if add_vehicle:
            
            # Seleccionar un carril aleatorio
            lane = random.choice(lanes)
            
            # Seleccionar una imagen aleatoria del vehículo
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)
    
    # Hacer que los vehículos se muevan
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        
        # Retirar el vehículo una vez que se sale de la pantalla
        if vehicle.rect.top >= height:
            vehicle.kill()
            
            # Sumar a la puntuación
            score += 1
            
            # Acelerar el juego después de pasar 5 vehículos
            if score > 0 and score % 5 == 0:
                speed += 1
    
    # Dibujar los vehículos
    vehicle_group.draw(screen)
    
    # Mostrar la puntuación
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 400)
    screen.blit(text, text_rect)
    
    # Comprobar si hay una cabeza en colisión
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
            
    # Juego de exhibición sobre
    if gameover:
        screen.blit(crash, crash_rect)
        
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Y or N)', True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect)
            
    pygame.display.update()

    # Esperar a que la entrada del usuario se reproduzca o salga
    while gameover:
        
        clock.tick(fps)
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                gameover = False
                running = False
                
            # Obtener la entrada del usuario (y o n)
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # Reiniciar el juego
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    # Salir de los bucles
                    gameover = False
                    running = False

pygame.quit()