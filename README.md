# Documentation of my code

# Introduction

The "Car Game" is an exciting racing game created by Jonatan Novoa using the Python programming language and the Pygame library. Immerse yourself in an experience full of speed, challenges, and adrenaline as you make your way through a busy highway teeming with moving vehicles.

In this game, you take on the role of a fearless driver navigating the bustling city streets in your speedy car. Your goal is to dodge oncoming vehicles as you progress along the road, accumulating points and testing your driving skills.

Get ready to face an increasingly challenging ordeal as the speed ramps up and vehicles become more numerous. Do you have what it takes to go as far as possible and claim your spot at the top of the leaderboard?

Strap yourself in, fire up the engine, and get ready for an exhilarating race in the "Car Game By Jonatan Novoa"!

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


