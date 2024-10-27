## 🟡 Vampire survivor

<br>
<br>

## 🟦 Intro


#### [4:20:28](https://youtu.be/8OMghdHP-zs?si=ePWx_BACyResw16v&t=15628)

<br>
<br>
<br>


## 🟦 Creating Levels with `Tiled`



### 🟠 Creating engaging levels is a key part of game development, and using a tile editor can streamline this process significantly.


>   In this lesson, we'll focus on using ✋ [Tiled/  mapeditor.org ](https://www.mapeditor.org/), a powerful and user-friendly tile `map editor`, to design levels for your Pygame projects. We'll explore why you need a tile editor, how to get started with Tiled, and how to import your tile maps into Pygame seamlessly.



<br>

## 🟠 Why Use a Tile Editor?

>#### When building a game level, having a visual representation of your design is crucial.



### 🟩 A tile editor allows you to:



**Visualize Your Design:** Place tiles and see how they come together in real-time, making it easier to tweak your layout.

**Efficiently Organize Tiles:** Use a grid system to manage your tiles, making it simpler to create complex environments without getting lost in code.

**Speed Up Development:** Quickly iterate on designs and test them without needing to dive into the code each time.



### 🟧 Introducing Tiled

#### Among the various tile editors available, Tiled stands out for its versatility and ease of use.

> #### You can download Tiled for free from [Tiled/  mapeditor.org ](https://www.mapeditor.org/).

It supports a range of features that make it suitable for both beginners and experienced developers.


### 🟢 Key Features of Tiled

**Layer Management:** Organize your tiles into layers for backgrounds, collisions, and foreground elements.

**Custom Properties:** Assign properties to tiles for better interaction with your game logic.

**Export Options:** Save your maps in a format that's easy to import into Pygame.



<br>

## 🟠 Importing Tile Maps into Pygame

### In this tutorial, we will specifically focus on how to import tile maps created in Tiled into Pygame.

> #### 🔴 While we won't delve into designing maps, understanding how to integrate them into your game is essential for creating immersive levels.

<br>


## 🟠 Resources for Further Learning

#### To enhance your understanding of tile maps and how to work with them in different engines, check out these helpful tutorials:

<br>

- [A guide to level creation with Tiled [ + how to use it with pygame ]](https://www.youtube.com/watch?v=N6xqCwblyiw&ab_channel=ClearCode)

<br>

#### Other:

[Use the TileMap to Make Incredible Maps & Levels for your Godot Games](https://youtu.be/rckLxmH_fK0?si=zne4yC7x3mpkTkCf)

[How to Use the New TileMap in Godot 4](https://youtu.be/tQSL2scuqeU?si=nZyaE7TlClHn5Xms)

[How to build a Tile Set Map Editor using HTML Canvas](https://youtu.be/IYgZMIB7_PM?si=Vn9hG-S4vnEq9ekb)

<br>

---


<br>
<br>
<br>

## 🟡 1. Installing Tiled via the Terminal


#### If you've faced issues downloading Tiled from the official website, a reliable alternative is to install it through the `terminal` using Snap.

🔴 This method is straightforward and helps avoid potential errors.

### Here’s how to do it:


#### 🔶 a: Install Tiled
To install Tiled, simply open your terminal and run the following command:

```python
sudo snap install tiled
```

#### 🔶  b: Launch Tiled

Once the installation is complete, you can run Tiled by typing:

```python
tiled
```
#### 📌 Pin Tiled to Your Desktop (optional)

For quick access, you may want to pin Tiled to your desktop or taskbar. This can typically be done by right-clicking the Tiled icon in your applications menu and selecting the option to pin it.



<br>
<br>

## 🟡 2.  Customizing the Editor Background Color and Tile Colors

#### One of the first steps in personalizing your workspace in Tiled is adjusting the editor's background color and tile colors. This can enhance visibility and make your design process more enjoyable.

### 🟢 Changing the Background and Tile Colors

🌈 **In the image below**, you can see that I have already made some adjustments to the settings. Customizing these colors can help you better visualize your project as you work.

### 🟢 Project Structure Overview

As you **customize your settings**, you’ll also notice a glimpse of the project structure. While the tile map has been created by the instructor, you have the option to build one from scratch.


<br>

### 🟧 Create your own tile map

If you want to learn how to create your own tile map, check out the video:[A guide to level creation with Tiled [ + how to use it with pygame ]](https://www.youtube.com/watch?v=N6xqCwblyiw&ab_channel=ClearCode). **It provides** helpful insights on using Tiled with Pygame


<br>

[<img src="tiled_00_map_beginner.gif"/>]()

>I already edited the colors of my editor

<br>
<br>

<br>
<br>

# 🟫 Important Points

 I’ll highlight the key aspects here, but please **watch the video tutorial** as the teacher will give a quick introduction to tile maps.

 <br>


# 🟧 Understanding the Project with the `World.tmx` File

 When you look at the map tiles, keep these points in mind:



### 🟤 Positioning:

- - Each tile has an `X` position and a `Y` **position**.

-  - The surface of the tile **can be different at the edges**.

- - **For example**, a tile may be fully grass, but at one corner, it could overlap with a rock.



### 🟤Grid System:

-  - The grid doesn’t use pixel coordinates, so we need to convert our positions accordingly.

<br>
<br>

# 🟧 Tile Positions on the Grid

## 🟤 In the grid:

### The tile at the very top left corner has the position (0, 0).

If you move to the tile directly to the right of it, the position changes to (1, 0).

[<img src="position-of-the-tile-on-the-grid__00.png"/>]()


### 🔴This means:

- - **The first number (X)** increases as you move right.

>-  - -  the first tile at the top , has the position of 0,0, if you go to the right of this tile 1 (lets say the second tile to the right), the number would be 1,0


- - **The second number (Y)** stays the same if you’re only moving horizontally.


> ### Remember, as you navigate the grid, the positions are defined by their distance from the origin point (0, 0).

<br>




<br>
<br>
<br>

---

<br>

# 🟡  Importing Your Grid Map into Pygame: Let's Get Started!

### Whether you want to create a stunning platformer or an adventurous RPG, importing your grid map is the first step!


### 🟦 Let’s dive into two ways to do this.

<br>

### 🟤 Method 1: Importing with a CSV File

#### You can use a CSV (Comma-Separated Values) file to import your grid map.

- - 🔴 While this method works, it can be quite tedious(it can feel a bit like a puzzle with too many pieces).

- - #### It involves a lot of manual setup and can be quite time-consuming.Picture yourself meticulously arranging each tile—definitely a lot of work!



<br>

### 🟤 Method 2: Discover the Power of Pytmx!

#### Instead of wrestling with CSV files, let’s use the super handy `pytmx module`.

- - #### This tool makes loading TMX files (the cool format for tile maps) into Pygame easy!  ✨


### 🌈 Installation



**Step 1:** Install `Pytmx`

- Open your terminal (or command prompt).

Type this command and hit Enter:

```python
pip install pytmx
```


<br>



---

<br>
<br>
<br>


## 🟦 Lets start coding

### We’ll use the `pytmx module` to `load a tile map` into our Pygame project. Let’s break it down step by step.


<br>

## 🟡 1: Import Pytmx


**First,** we need to import the necessary function from `pytmx`. This function will help us load our map file.


```python
from pytmx.util_pygame import load_pygame
```

<br>
<br>

## 🟡 2: Create a Setup Method in the Game Class

**Next**, we’ll **create a new method** in your `Game` **class** called `setup()`.

> #### This method will be responsible for loading our map.

Here’s how to do it:

```python
def setup(self):
    map = load_pygame()
```

