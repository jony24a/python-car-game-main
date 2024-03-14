import pygame

from Vehicle import Vehicle

class PlayerVehicle(Vehicle):
    
    def __init__(self, x, y):
        image = pygame.image.load('images/carro.png')
        super().__init__(image, x, y)