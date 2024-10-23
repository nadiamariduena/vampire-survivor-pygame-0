## 🟡 Vampire survivor



<br>
<br>
<br>

## 🟦 Intro





[3:47:56](https://youtu.be/8OMghdHP-zs?si=Q9UgY9U1Et1Ck8mf&t=13676)

<br>

## 🫐 🟡 Player Class Implementation

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



<br>
<br>


### 🟡  3.  Using the `Player` Class in `main.py`

Now that we have our Player class set up in player.py, we need to use it in the main game file (main.py).

To do this, we **import** the `Player` **class** like this:


