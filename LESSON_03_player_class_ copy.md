## 🟡 Vampire survivor





## 🟦 Intro



<br>
<br>
<br>

[3:47:56](https://youtu.be/8OMghdHP-zs?si=Q9UgY9U1Et1Ck8mf&t=13676)

<br>

# 🫐 🟡 Player Class Implementation

#### Develop a player class that utilizes an imported player image and allows for movement (should be implemented as a sprite).

---

<br>
<br>

## 🟡  1. Create the Player Class in a Separate Python File

- - **First,** open the code folder and create a new file named **`player.py`**.

- -  **Now**, we're going to **define the Player class**.

<br>

#### 🟧 A quick overview:

> #### Player is going to be a "sprite", which is just a character or object in your game.

> - - #### The `pygame.sprite.Sprite` is a special class that gives our player cool features like drawing, moving, and interacting with other sprites.

```python
 from settings import *  # We import the settings (like width & height) from the settings file.

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
# The 'super()' function is used to call the __init__ method of the parent class (Sprite).
# 🔴 We're only passing 'groups' here because that's the only thing we need from the parent.

        super().__init__(groups)

```

<br>

<!-- no public -->

### 🟢 Explanation of `super() and __init__`:


The `__init__` **method** is the **constructor** of the class—it runs when we create a new Player.

<br>

> #### The `super().__init__(groups)` is calling the parent class’s constructor (the one from `pygame.sprite.Sprite)` and passing the groups parameter.


>  🟤 You don’t need to pass the pos (position) to super() because it’s not required by pygame.sprite.Sprite.

#### The groups is all that matters for now—this tells Pygame where to put our player in the game’s sprite groups.
<!-- no public -->

<br>
<br>

## 🟡  2. Import the images

### In this project, we’ll be working with many more images compared to our first game.

> #### 🟤 These images are organized in folders, and some folders even contain other folders.



####  So, we need to know how to correctly navigate through these folders to find the images we need.

Here’s how you can load an image for the player character:

```python
from settings import *  # This imports the settings, like width & height

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
# This loads the player's image from a folder path.
# The 'join()' function helps us navigate through the folders correctly.

        self.image = pygame.image.load(join("images", "player", "down", "0.png" )).convert_alpha()


        # pos of the img
        self.rect = self.image.get_frect(center = pos)
```
> **convert_alpha()** don't forge to convert to alpha

### in my code

```python
self.image = pygame.image.load(join("../images", "player", "down", "0.png" )).convert_alpha()
```

<a name="check-the-path_"></a>

#### Because my structure is:

```python
project_folder/
│
├── code/             # The folder where your 'main.py' is located
│   └── main.py
│
├── .venv/            # Virtual environment folder (if using one)
│
└── images/           # Folder where all your game images are stored
    ├── player/
    │   ├── down/
    │   │   └── 0.png
    └── other_image.png

```



<br>

## 🟠 What’s Happening Here?

#### So when you use:

```python
join("image", "player", "down", "0.png")
```
#### It creates this full path:

```python
image/player/down/0.png
```
<br>

<!-- no public -->

**"image":** This is the main folder where all your game assets (like images) are stored.

**"player":** Inside the image folder, there’s another folder called player which holds all the player-related images.

**"down":** Inside the player folder, you have subfolders for different directions `(up, down, left, right)`.

- - In this case, it's the down folder because you’re showing the player’s down-facing sprite.


**"0.png":** Finally, you choose a specific image (like a frame of an animation) from the down folder. Here, 0.png is the first image in that folder.


 <!-- no public -->


<br>
<br>


### 🟡  3.  Using the `Player` Class in `main.py`

Now that we have our Player class set up in player.py, we need to use it in the main game file (main.py).

To do this, we **import** the `Player` **class** like this:



```python
from player import Player
```

<br>

### 🟡  4. Create an Instance of the `Player` Class

- To actually use the **`Player` class**, we need to create an **instance of it**.


```python
# ---- PLAYER
self.player = Player()
```
>Think of an instance like a "real" player character in the game. You can create one like this:


<br>

### 🟢  But, remember, the Player class needs a couple of things to work properly

  **Specifically**:

- - the **position** and **groups** we passed in the `__init__()` method earlier:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
```
>#### So, we need to pass both the position (where the player starts) and the groups (to organize our sprites) when we create the player instance.


<br>
<br>

### 🟡  5. Passing the Player Parameters Inside the Game Class


#### 🟤 1. Position (pos)

The first thing we need is the position of the player on the screen.

> **For example**, if we want the player to start at coordinates (400, 300), we create the player like this:

```python
# ---- PLAYER
self.player = Player(400, 300)
```

#### 🟤 2. Groups (groups)

**Next**, we need to pass the group.

>This is a list of all sprites that will be managed together.

- - We’ll create this group later, but for now, we just pass `self.all_sprites` as the group for the player.

```python
        # ---- PLAYER
        self.player = Player((400, 300), self.all_sprites)
```

<br>
<br>

### 🟡  6. Create the First Group

#### We now need to create the group where all our sprites (like the player) will go.

> - #### To create an empty group, we can use this:

```python
self.all_sprites = pygame.sprite.Group()
```

### Putting It All Together

Here’s how everything works in the Game class:

```python
from settings import *
from player import Player 🟡

# Define the Game class to encapsulate the game's functionality
class Game:
    def __init__(self):
        # Initialize all pygame modules
        pygame.init()


        # --- SETUP ------
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Survivor')
        self.clock = pygame.time.Clock()
        self.running = True
        # --- SETUP ------

        # GROUPS 🟡
        self.all_sprites = pygame.sprite.Group()

        # SPRITES 🟡
        # player
        self.player = Player((400, 300), self.all_sprites)

```
<br>
<br>

### 🟡  8. Updating and Drawing Sprites

#### In your game, you need to update and draw the sprites every frame.

- Here are the two important lines that do that:


```python
# Update all the sprites (so they can move, change, etc.)
self.all_sprites.update(dt)

# Draw all the sprites on the screen
self.all_sprites.draw(self.display_surface)

```


<br>

###  🟠  Putting It All Together
Here’s the complete code, with the update and draw functions included:

```python
# Import all settings defined in the settings.py file
from settings import *
from player import Player

# Define the Game class to handle the game's logic
class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # --- SETUP ------
        # Set up the game window size
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # Set the window title
        pygame.display.set_caption('Survivor')
        # Set up the clock to control the game's speed
        self.clock = pygame.time.Clock()
        # A flag to control the game loop
        self.running = True
        # --- SETUP ------

        # GROUPS
        self.all_sprites = pygame.sprite.Group()

        # SPRITES
        # Create the player character and add it to the sprite group
        self.player = Player((400, 300), self.all_sprites)

    def run(self):
        # Main game loop
        while self.running:
            # Get the time passed since the last frame
            dt = self.clock.tick() / 1000

            # Handle events (like pressing keys or closing the window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Exit the loop

            # Update the game state (move characters, check for collisions, etc.)
            self.all_sprites.update(dt)

            # Draw all the sprites (player, enemies, etc.) onto the screen
            self.all_sprites.draw(self.display_surface)

            # Refresh the screen with the new frame
            pygame.display.update()

        # Quit Pygame when the loop ends
        pygame.quit()

# Start the game
if __name__ == '__main__':
    # Create an instance of the Game class and start the game loop
    game = Game()
    game.run()

```

### output


#### [3:55:47](https://youtu.be/8OMghdHP-zs?si=wDCy8A7FL5SkuW3A&t=14147)

[<img src="setup_player-game_00.png"/>]()

>   🔴 **If the game window closes when running python main.py, try this:** Make sure you're inside the `.venv` (virtual environment) and that `pygame and pygame-ce` are installed. If it still doesn’t work, double check the image path. Since `main.py` is in the code folder, the path might need to go up one folder level to access the images. ✋ [Go to section](#check-the-path_)



 <br>

<!-- no public -->

### 🟠 Explanation:

**Update:** `self.all_sprites.update(dt)` moves and changes the sprites, like making the player move or updating animations.

**Draw:** `self.all_sprites.draw(self.display_surface)` makes sure all sprites are shown on the screen for the current frame.

> #### These lines make sure everything that should change (like the player or enemies) gets updated and that everything is shown on the screen.
<!-- no public -->

<br>
<br>

---

<br>