# Documentation of my code

# Introduction

The "Car Game" is an exciting racing game created by Jonatan Novoa using the Python programming language and the Pygame library. Immerse yourself in an experience full of speed, challenges, and adrenaline as you make your way through a busy highway teeming with moving vehicles.

In this game, you take on the role of a fearless driver navigating the bustling city streets in your speedy car. Your goal is to dodge oncoming vehicles as you progress along the road, accumulating points and testing your driving skills.

Get ready to face an increasingly challenging ordeal as the speed ramps up and vehicles become more numerous. Do you have what it takes to go as far as possible and claim your spot at the top of the leaderboard?

Strap yourself in, fire up the engine, and get ready for an exhilarating race in the "Car Game By Jonatan Novoa"!

# Code Structure

1. Main Script (juego.py):

- This script serves as the entry point of the game.
- It initializes the Pygame engine, sets up the game window, and handles the game loop.
- Responsible for managing events, updating game logic, drawing game elements, and checking for collisions.
- Imports the PlayerVehicle and Vehicle classes from separate files.
- Contains the main loop that runs the game.
  
2. PlayerVehicle Class (PlayerVehicle.py):

- Represents the player-controlled vehicle in the game.
- Inherits from the Vehicle class.
- Initializes the player's vehicle with its image and initial position.
- Handles movement of the player's vehicle based on user input.

3. Vehicle Class (Vehicle.py):

- Represents non-player vehicles in the game.
- Initialized with a random image and initial position.
- Handles movement of vehicles across the screen.
- Detects collisions with the player's vehicle.

4. Other Files:

- The game might include additional files for images, sounds, or other resources used in the game.

# Main Classes

1. juego.py:

- This class represents the main script of the game.
- It initializes the Pygame engine, sets up the game window, and manages the game loop.
- Handles events, updates game logic, draws game elements, and checks for collisions.
- Contains the main loop that runs the game.
  
2. PlayerVehicle (defined in PlayerVehicle.py):

- Represents the player-controlled vehicle in the game.
- Inherits from the Vehicle class.
- Initializes the player's vehicle with its image and initial position.
- Manages movement of the player's vehicle based on user input.
  
3. Vehicle (defined in Vehicle.py):

- Represents non-player vehicles in the game.
- Initialized with a random image and initial position.
- Manages movement of vehicles across the screen.
- Detects collisions with the player's vehicle.

# Game Operation 

1. Initialization:

- The game initializes by launching the main script (juego.py).
- Pygame engine is initialized, and the game window is set up.
- Necessary resources like images and sounds are loaded.
  
2. Game Loop:

- The main game loop begins, continuously running until the game is exited.
- Within the loop, events such as user inputs are handled.
- Game logic is updated, including the movement of vehicles and detection of collisions.
- Game elements are redrawn on the screen to reflect the updated state.
  
3. Player Interaction:

- The player controls their vehicle using keyboard input (left and right arrow keys).
- The player's vehicle moves horizontally within predefined lanes on the road.
  
4. Vehicle Movement:

- Non-player vehicles are generated and move vertically downward on the screen at varying speeds.
- New vehicles are added to the game to maintain a constant flow of traffic.
- Vehicles are removed from the game when they move beyond the screen.
  
5. Collision Detection:

 - Collision detection is performed between the player's vehicle and other vehicles on the road.
 - If a collision occurs, the game ends, and a "Game Over" message is displayed.
   
6. Scoring:

- The player earns points as they successfully navigate through the traffic without colliding with other vehicles.
- The game speed increases periodically or based on the player's score to ramp up the difficulty.
  
7. Game Over:

- When a collision occurs or the player chooses to quit the game, the game over sequence is initiated.
- The final score is displayed, along with an option to restart the game.
  
8. Restart:

The player can choose to restart the game by pressing a designated key (typically 'Y' or 'N') when prompted.
If the player chooses to restart, the game resets, and the main loop continues from the beginning.

# Conclusion

The "Car Game By Jonatan Novoa" delivers an engaging and challenging gaming experience. With its fast-paced gameplay, intuitive controls, and progressively increasing difficulty, players are drawn into an immersive world of traffic navigation. Interactive features like collision detection and scoring system add depth to the gameplay, while the user-friendly interface ensures accessibility for players of all skill levels. Overall, the game showcases creativity and innovation in design, offering hours of entertainment for gaming enthusiasts.

# Data Dictioonary

In the context of the "Car Game By Jonatan Novoa," a data dictionary might include the following:

1. PlayerVehicle Class:

- image: Represents the image of the player-controlled vehicle.
- rect: Represents the rectangular area occupied by the player's vehicle on the screen.
- x: Represents the x-coordinate of the player's vehicle.
- y: Represents the y-coordinate of the player's vehicle.
  
2. Vehicle Class:

- image: Represents the image of a non-player vehicle.
- rect: Represents the rectangular area occupied by a non-player vehicle on the screen.
- x: Represents the x-coordinate of a non-player vehicle.
- y: Represents the y-coordinate of a non-player vehicle.
- speed: Represents the speed of a non-player vehicle.
- score: Represents the player's score in the game.

3. Main Script (juego.py):

- width: Represents the width of the game window.
- height: Represents the height of the game window.
- screen: Represents the Pygame display surface.
- player_group: Represents the group containing the player's vehicle sprite.
- vehicle_group: Represents the group containing non-player vehicle sprites.
- clock: Represents the Pygame clock object for managing frame rate.
- fps: Represents the target frames per second for the game.
- gameover: Represents the flag indicating whether the game is over.
- running: Represents the flag indicating whether the game is running.

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

# How to play the game

To play the "Car Game By Jonatan Novoa," follow these instructions:

1. Starting the Game:

- Launch the game by running the main script (juego.py).
- The game window will appear, displaying the road and your vehicle.
  
2. Controls:

- Control your vehicle using the left and right arrow keys on your keyboard.
- Use the left arrow key to move your vehicle to the left lane.
- Use the right arrow key to move your vehicle to the right lane.
  
3. Avoid Collisions:

- Navigate your vehicle through the traffic, avoiding collisions with other vehicles.
- Colliding with another vehicle will end the game.
  
4. Scoring:

- Score points by successfully maneuvering through traffic without colliding.
- The longer you survive without crashing, the higher your score will be.

5. Game Over:

- The game will end when you collide with another vehicle.
- A "Game Over" message will be displayed, along with your final score.

6. Restarting the Game:

- If you wish to play again, press the 'Y' key when prompted.
- The game will reset, and you can start a new round.

7. Exiting the Game:

- If you want to quit the game, press the 'N' key when prompted.
- The game window will close, and you'll return to the desktop.
  
8. Enjoy the Game:

- Have fun playing the "Car Game By Jonatan Novoa" and aim for a high score!
  
By following these instructions, you can enjoy an exciting and challenging gaming experience in the world of fast-paced traffic navigation. Good luck!

# Character Movement

In the "Car Game By Jonatan Novoa," character movement is controlled by the player using the left and right arrow keys. The player's vehicle starts in the center lane and can move left or right to avoid collisions with other vehicles. Continuous forward movement is automatic, and the player earns points by navigating through traffic without crashing. Collisions end the game, and players aim to achieve high scores by mastering lane-changing maneuvers.


