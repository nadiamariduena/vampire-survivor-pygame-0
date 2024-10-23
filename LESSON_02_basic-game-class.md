## 🟡 Vampire survivor

 <br>
<br>
<br>

## 🟦 Intro





[3:47:56](https://youtu.be/8OMghdHP-zs?si=Q9UgY9U1Et1Ck8mf&t=13676)

<br>

## 🟡  1. GAME Class Implementation

> #### In our code folder, you’ll find the `main.py` and `settings.py` files.

- The `settings.py` file includes the following configuration, which is referenced in main.py:

```python
import pygame
from os.path import join
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
TILE_SIZE = 64
```

<br>
<br>


## 🟧 Transitioning to a More Organized Framework

<br>

### 🟤 Comparing the previous approach (Space Shooter)

In the new code structure **(the code below)**, we see a shift towards encapsulating game logic within a dedicated Game class, which is a significant change from the previous approach [check the end of the page](https://github.com/nadiamariduena/python-intro-2024-privat/blob/master/z_PYgame/spaceship_game/RE_game-CODE_17_Debut-game_create_Sounds.md) .

- - This organization promotes better code management and readability by grouping related functionality.

> - - #### The use of instance methods, like run, allows for clearer separation of the game loop, event handling, updating, and rendering processes.


### In contrast to the previous script...

- In contrast to the previous script where functionality was spread throughout, this class based approach enhances modularity, making it easier to expand and maintain the game in the future.

<br>

> Additionally, encapsulating game state (like running and display_surface) within the Game class supports better control over the game's lifecycle.

 Overall, this design pattern aligns with best practices in game development, paving the way for more complex features as we continue building the "Vampire Survivor" project.

<br>

## 🟡 2.  Define a Game class that initializes the `Pygame` library and sets up the game window.

<br>

```python
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)

        pygame.display.set_caption('Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while  self.running:

            # DT

            # EVENT loop

            # Update

            # draw
```

<br>

#### The `__init__` **method** is called when an instance of the class is created, ✋ where it initializes `Pygame`, creates the display surface, sets the window title, initializes a clock for frame rate management, and establishes a running state for the game loop.

<br>

> #### The run method contains a loop that will continuously execute as long as the running variable is set to True.

- Within this loop, placeholders indicate where the **delta time calculation, event handling, game state updates, and rendering** would take place, ensuring a structured approach to the game’s main loop.


<br>

### Updated code

- 🔴 When we run this code, it will display a black screen.

```python
from settings import *  # Import settings, including WINDOW_WIDTH, WINDOW_HEIGHT, and any other configurations.

class Game:  # Define the Game class.
    def __init__(self):  # Constructor method for initializing the game.
        pygame.init()  # Initialize the Pygame library.

        # Set up the display surface with specified window dimensions.
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        pygame.display.set_caption('Survivor')  # Set the window title to 'Survivor'.
        self.clock = pygame.time.Clock()  # Create a clock object to manage frame rate.
        self.running = True  # Set a flag to indicate that the game is running.

    def run(self):  # Define the run method to contain the game loop.
        while self.running:  # Keep looping while the game is running.

            # Calculate the delta time for frame-independent movement.
            dt = self.clock.tick() / 1000

            # Handle event loop to check for user interactions.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check if the quit event is triggered.
                    self.running = False  # Set running to False to exit the game loop.

            # Update logic goes here, where game state changes would be implemented.

            # Draw logic goes here, where game elements would be rendered to the screen.
            pygame.display.update()  # Update the display to show the latest frame.

        pygame.quit()  # Quit Pygame and clean up resources.

# Instantiate the Game class and call the run method to start the game.
game = Game()
game.run()  # Start the game loop.

```

<br>
<br>
<br>

---


# 🔴 Note:

## 🟡 Simplifying Execution in Our Project

#### One key aspect of our project is that we will create multiple files as we develop the game.

- To streamline our workflow, we want to ensure that we only need to run the `main.py` file to execute the entire game.

<br>


[3:51:37](https://youtu.be/8OMghdHP-zs?si=GwAqCM2--qjptW0C&t=13897)



### This means that all necessary components like settings, game logic, and any other modules should be structured in a way that they are automatically imported and utilized when we run main.py.

> - - #### 🌈  (This means that main.py should include code that pulls in everything we need from the other files)


#### This approach not only simplifies the execution process but also enhances the organization of our code, allowing us to focus on development without the need to run each file individually.



## 🟡 3.  Using Conditional Execution for Game Development



#### The line if `__name__ == '__main__':` is important because it ensures that the code inside it only runs when `main.py` is executed directly, not when it's imported as a module in another file.

<br>

```python
#  code at  the bottom of every file
if __name__ == '__main__':
     game = Game()
     game.run()
```

> #### This means that `if someone imports this file` to use its classes or functions in a different program, `the game will not automatically start`.

#### By placing `game = Game()` and `game.run()` <u>inside this conditional</u> , we can control when the game starts, making our code more flexible and preventing unintended execution.

#### This practice helps maintain a clean and organized project structure.

---


## 🟦 Before moving on

### We now have a basic game class

```python
# Import all settings defined in the settings.py file
from settings import *

# Define the Game class to encapsulate the game's functionality
class Game:
    def __init__(self):
        # Initialize all pygame modules
        pygame.init()

        # Create a display surface with the specified window dimensions
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Set the title of the game window
        pygame.display.set_caption('Survivor')

        # Create a clock to manage the game's frame rate
        self.clock = pygame.time.Clock()

        # Initialize a running flag to control the game loop
        self.running = True

    def run(self):
        # Main game loop that runs while the game is active
        while self.running:
            # Calculate the time since the last frame (in seconds)
            dt = self.clock.tick() / 1000

            # Handle events, such as user inputs and window actions
            for event in pygame.event.get():
                # Check if the user wants to quit the game
                if event.type == pygame.QUIT:
                    self.running = False  # Set running to False to exit the loop

            # Update game state (placeholder for future updates)

            # Draw the current frame to the display
            pygame.display.update()

        # Quit all pygame modules when the game loop ends
        pygame.quit()

# Check if this script is being run directly (not imported)
if __name__ == '__main__':
    # Create an instance of the Game class
    game = Game()
    # Start the game loop
    game.run()

```

### Next step i will be creating the player class