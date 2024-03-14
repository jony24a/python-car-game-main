# Flowchart


```mermaid
graph TD;
    A[Start] --> B{Is player pressing a key?};
    B -->|Yes| C[Execute corresponding action];
    C --> D{Does action cause player movement?};
    D -->|Yes| E{Does player collide with obstacle?};
    E -->|Yes| F[Display Game Over screen];
    F --> G{Does player press 'Y' to play again?};
    G -->|Yes| A;
    G -->|No| H[Quit game];
    E -->|No| I{Does player reach the goal?};
    I -->|Yes| J[Display Victory screen];
    J --> G;
    I -->|No| D;
    D -->|No| B;
    B -->|No| K{Has level time limit elapsed?};
    K -->|Yes| F;
    K -->|No| B;
    B -->|Yes| L{Is game paused?};
    L -->|Yes| M[Display pause menu];
    L -->|No| B;
    M --> N{Does player select continue?};
    N -->|Yes| B;
    N -->|No| O[Quit to main menu];
    O -->|Yes| A;
    O -->|No| H;

```
# Class Diagram
```mermaid

classDiagram
    class PlayerVehicle {
        -image: pygame.Surface
        +__init__(x: int, y: int)
    }
    class Vehicle {
        -image: pygame.Surface
        +__init__(image: pygame.Surface, x: int, y: int)
    }
    class juego {
        -pygame: Module
        -width: int
        -height: int
        -screen_size: tuple
        -screen: pygame.Surface
        -gray: tuple
        -green: tuple
        -red: tuple
        -white: tuple
        -yellow: tuple
        -road_width: int
        -marker_width: int
        -marker_height: int
        -left_lane: int
        -center_lane: int
        -right_lane: int
        -lanes: list
        -road: tuple
        -left_edge_marker: tuple
        -right_edge_marker: tuple
        -lane_marker_move_y: int
        -player_x: int
        -player_y: int
        -clock: pygame.time.Clock
        -fps: int
        -gameover: bool
        -speed: int
        -score: int
        -player_group: pygame.sprite.Group
        -vehicle_group: pygame.sprite.Group
        -image_filenames: list
        -vehicle_images: list
        -crash: pygame.Surface
        -crash_rect: pygame.Rect
    }
    
    PlayerVehicle --|> Vehicle
    juego --|> pygame.Surface
    juego --|> pygame.time.Clock
    juego --|> pygame.sprite.Group


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


# Diagram of sequence
```mermaid
sequenceDiagram
    participant Main
    participant PlayerVehicle
    participant Vehicle
    participant CollisionDetection
    participant ScoreManager

    Main ->> PlayerVehicle: Start game
    PlayerVehicle ->> Vehicle: Create player vehicle
    loop Game in progress
        Main ->> Main: Control game loop
        Main ->> PlayerVehicle: Handle player input
        PlayerVehicle ->> PlayerVehicle: Move player vehicle

        alt Collision detected
            PlayerVehicle ->> CollisionDetection: Check collision
            CollisionDetection ->> Main: Inform collision
            Main ->> Main: Handle collision
        else No collision
            Main ->> Vehicle: Move computer-controlled vehicles
        end

        alt Check for points
            Vehicle ->> ScoreManager: Check score
            ScoreManager ->> Main: Inform about score
            Main ->> Main: Update score
        end
    end
```


