
# class Diagram
```mermaid

classDiagram
    class Vehicle {
        - image
        - rect
        + __init__(image, x, y)
    }
    class PlayerVehicle {
        - __init__(x, y)
    }
    class Main {
        - game_loop()
    }

    Main --> Vehicle
    Main --> PlayerVehicle

```

# Class de secuencia 
```mermaid
sequenceDiagram
    participant Main
    participant PlayerVehicle
    participant Vehicle
    participant CollisionDetection
    participant ScoreManager

    Main ->> PlayerVehicle: Iniciar juego
    PlayerVehicle ->> Vehicle: Crear vehículo del jugador
    loop Juego en curso
        Main ->> Main: Controlar bucle del juego
        Main ->> PlayerVehicle: Manejar entrada del jugador
        PlayerVehicle ->> PlayerVehicle: Mover vehículo del jugador

        alt Detectar colisión
            PlayerVehicle ->> CollisionDetection: Verificar colisión
            alt Colisión detectada
                CollisionDetection ->> Main: Informar colisión
                Main ->> Main: Manejar colisión
            end
        else No hay colisión
            Main ->> Vehicle: Mover vehículos controlados por la computadora
        end

        alt Verificar puntos
            Vehicle ->> ScoreManager: Verificar puntaje
            alt Se obtienen puntos
                ScoreManager ->> Main: Informar sobre puntaje
                Main ->> Main: Actualizar puntaje
            end
        end
    end
```

# Class identidad relacion 

```mermaid
erDiagram
    PLAYER {
        string player_id
        string player_name
        int score
    }
    VEHICLE {
        string vehicle_id
        string vehicle_type
        string vehicle_image
    }
    PLAYER_VEHICLE {
        string player_id
        string vehicle_id
        int position_x
        int position_y
    }
    OBSTACLE {
        string obstacle_id
        string obstacle_type
        string obstacle_image
    }
    PLAYER_OBSTACLE {
        string player_id
        string obstacle_id
        int position_x
        int position_y
    }

    PLAYER ||--o{ PLAYER_VEHICLE : owns
    PLAYER_VEHICLE }o--|| VEHICLE : controls
    PLAYER_VEHICLE ||--|{ PLAYER_OBSTACLE : encounters
    PLAYER_OBSTACLE }|--|| OBSTACLE : obstructs

```

# Diagrama de flujo 

```mermaid
graph TD;
    A[Comenzar] --> B{¿Jugador presiona una tecla?};
    B -->|Sí| C[Ejecutar acción correspondiente];
    C --> D{¿Acción produce movimiento del jugador?};
    D -->|Sí| E{¿Jugador colisiona con obstáculo?};
    E -->|Sí| F[Mostrar pantalla de Game Over];
    F --> G{¿Jugador presiona 'Y' para jugar de nuevo?};
    G -->|Sí| A;
    G -->|No| H[Salir del juego];
    E -->|No| I{¿Jugador alcanza la meta?};
    I -->|Sí| J[Mostrar pantalla de victoria];
    J --> G;
    I -->|No| D;
    D -->|No| B;
    B -->|No| K{¿Transcurrido tiempo límite del nivel?};
    K -->|Sí| F;
    K -->|No| B;
    B -->|Sí| L{¿Juego en pausa?};
    L -->|Sí| M[Mostrar menú de pausa];
    L -->|No| B;
    M --> N{¿Jugador selecciona continuar?};
    N -->|Sí| B;
    N -->|No| O[Salir al menú principal];
    O -->|Sí| A;
    O -->|No| H;
```