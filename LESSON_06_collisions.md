
## 🟡 Vampire survivor



<br>
<br>


## 🟦 Intro




#### [4:00:25](https://youtu.be/8OMghdHP-zs?si=K8Dih6ZmFsOst1f4&t=14425)

<br>



# 🫐 🟡 <u>Collisions</u>  Implementation

#### 🌈 We previously covered this topic in our first game project. You can refer to the steps outlined [collisions](https://github.com/nadiamariduena/python-games-01/blob/beginner-00-deafult-install-and-games/0_SPACESHIP-game/RE_game-CODE_12_Debut-game_create_collision.md)  for a detailed guide.

<br>
<br>

## 🟠 Rectangular Collision Logic: Identifying Contact vs. Overlap

 **Rectangles, or "rects,"** can only tell us when they’re touching, but they don’t say what to do next.

> #### To make the game interesting, we need to use that collision info to move the player around when they hit something. Let’s make those collisions work!




<br>

>In the image below, you'll see four boxes. In the first example, the player’s box overlaps with the obstacle’s box. In the second example, the player and the obstacle are touching, but they don’t overlap.


[<img src="collision_00__overlaping.png"/>]()

>Images source: Master Python by making 5 games **[the new ultimate introduction to pygame]**

<br>

#### [4:01:39](https://youtu.be/8OMghdHP-zs?si=QiA4CxKXIDEjB5vb&t=14499)

## 🔴 The complication

#### When a collision happens, we can’t tell exactly where it’s occurring. It could be at the bottom, the top, or any side of the player. Check out the image below for a clearer idea!


<br>

## 🟧 Finding the Collision Side


### To figure out where the collision is happening, we need to break it down:

> ####  We <u>check for collisions separately</u>  on the horizontal (left and right) and vertical (up and down) axes.


<br>

### 🌈 let’s go one by one!

- We’ll **check from left to right** to observe how the player interacts with obstacles.

> - - This way, we can better understand the behavior of the collisions and determine how to respond to them effectively.

[4:02:40](https://youtu.be/8OMghdHP-zs?si=Uj8rhmTMwlaWYwyZ&t=14560)

[<img src="chec_collision_left_or_right.png"/>](https://youtu.be/8OMghdHP-zs?si=Uj8rhmTMwlaWYwyZ&t=14560)



<br>
<br>
<br>

---

## 🔴 Problems with this approach

### The main issue with this approach is that<u>it only works if a single object is moving</u>   (not the enemy),

<br>

> ### 🟥 for example at the moment the player can only collide with: trees, rocks and the hills (because they are static),

- ### 🔺 the player cannot collide with any of the enemies

since those are moving, the collision logic would break.

<br>

## 🟧 Collision between Two Moving Objects


### When we’re dealing with collisions between two moving objects, we need a bit more logic.

> #### Think of it like the way a [ parrot fish](https://youtu.be/zdzAUQ4juH4?si=zPQ-hA0ufLFrn9KV) creates a "bubble" around itself to protect from parasites.

This bubble is kind of like the hitbox we need for our objects. So, imagine this bubble in terms of X (left/right) and Y (top/bottom) coordinates.

When we’re checking if an enemy collides with the player, the enemy also has its own bubble.

#### 🟣  So, both the player and the enemy need these "bubbles" (hitboxes) to exchange collision information.


---

<br>
<br>
<br>

## 🟡 Guide to Setting Up Collision Detection with Moving Objects


### In this section, we'll walk through the process of adding collision detection between the player and other sprites in your game.

> #### You'll learn how to create and manage collision objects like blocks, randomize their positions and sizes, and set up a system to check for overlaps between the player and these objects.

#### 🟧 This will allow your game to respond when the player hits or interacts with obstacles.



### Summary:

- **Create sprites.py:** A file to store your block (and other) sprites.

- **Set Up Block Sprite:** Define a basic blue block (hitbox) that the player will collide with.

- **Import the Sprite:** Add the sprite class to main.py.

- **Create Instances:** Spawn several blocks (or other objects) in the game world.

- **Randomize Positions and Sizes:** Use `randint()` to make the blocks appear in random spots and with random sizes.

- **Group the Sprites:** Store the blocks in a sprite group for easy collision checking later.

<br>
<br>

<br>
<br>

# 🟦 Lets get started:

## 🟡   Set Up Your Code Structure

### Right now, we don't have anything for the player to collide with.

> - #### 🍨 To fix this, we need to add some obstacles or blocks 🧊 to collide with.

#### So, let's create a new sprite (or rectangle) that we can use for collision.


<br>


##  🟡 1.  Create the `sprites.py` File

- #### First, create a new file called `sprites.py` in your `code` folder.

> - - This file will store all your sprite classes, like the player, enemies, and other objects (such as blocks) that the player can collide with.

<br>
<br>

## 🟡 2.  Set Up a Basic Block Sprite

### Now, let’s create a basic block 🧊 (a blue rectangle) that we can use for collisions.

```python
from settings import *

class CollisionsSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)

        # --- a blue block surface

        self.image = pygame.Surface(size)
        self.image.fill('blue')
        self.rect = self.image.get_frect(center = pos)
```


<br>

- #### This defines a new sprite (CollisionsSprite) that represents a block.

- #### It has a position (pos), size (size), and a rectangle (rect) that will help us detect collisions.


> #### 🟤 Note: At this point, the block’s position and size will be controlled from the main game (main.py), not here in sprites.py.

<br>
<br>

## 🟡 3.  Import the `Sprite` in `main.py`

#### In your `main.py` file, you need to import the CollisionsSprite class so you can use it.

```python
from sprites import *
```


<br>
<br>

## 🟡 4. Create Instances of the Collision Block

#### We now want to create multiple instances of the blue 🧊   block (or "collision blocks") in the game world.

<br>

> #### Let’s create 6 blocks for now.


```python
for i in range(6):
    CollisionsSprite(pos, size, self.all_sprites)
```
- **`pos`** is the position where each block will be placed.

- **`size`** defines the width and height of the block.

- **`self.all_sprites`** is the group of all sprites (including the player, enemies, etc.).

<br>

> #### 🟤 Note: We’ll randomize the position and size of these blocks later, so they appear in different locations and have different sizes.


<br>
<br>

## 🟡 5. Randomize the Position of the Blocks 🧊

### Now that we have the instances of the blue/rect

> ### Let’s add randomness so that the blue blocks appear in different locations on the screen each time the game runs.

#### 🟤 1. Import `randint` to generate random numbers:

```python
from random import randint
```

#### 🟤 2. Randomize the position in both the X and Y directions:

```python
x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
```

<br>

 **`WINDOW_WIDTH and WINDOW_HEIGHT`** are the dimensions of the game window.

> This will randomly place the blocks within the visible area of the screen.


#### Putting it together:

```python
   for i in range(6):

            x,y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)

            CollisionsSprite(pos, size, self.all_sprites)
```
<br>


#### 🟤3. Replace the position placeholder with the random values:

```python
# before
 CollisionsSprite(pos, size, self.all_sprites)

# after
 CollisionsSprite((x,y), size, self.all_sprites)
```

<br>

#### 🟤4) Randomize the block’s size

- We can also make the **blocks different sizes each time**.

> #### To do this, use randint() to generate random width and height:

```python
w,h = randint(60, 100), randint(50, 100)
# > 🔴 randint allows you to create boxes of different sizes each time the game runs.
```
#### 🟤5) Update the block creation with the random size:

```python
# before
CollisionsSprite((x,y), size, self.all_sprites)
# after
CollisionsSprite((x,y), (w,h), self.all_sprites)
```

[<img src="collision_00__randome_blue_boses-no-coll_yet.gif"/>]( )

> #### At the moment, there’s no collision detection in place, so the player passes right through the obstacle.


<br>
<br>


## 🟡 6. Add the Blocks to a New Group

### 🔴 We need a way to manage our collision blocks, so let's create a new sprite group.

> #### This `group` will help us keep track of all the blocks in one place.


 - 🍭 Create the collision group

```python
self.collision_sprites = pygame.sprite.Group()
# This group will contain all the CollisionsSprite objects, making it easier to check for collisions later on.
```
<br>

## 🟡 7. Add Blocks 🧊 to the Collision Group

### 🔴 Now that we have our collision group ready, we need to include it when creating our block sprites.

> #### This step connects the blocks to the group.


-  Modify the block creation line to include the new group

```python
CollisionsSprite((x,y), (w,h), (self.all_sprites, self.collision_sprites))
```

#### Here’s how it changes

```python
#before
CollisionsSprite((x,y), (w,h), self.all_sprites)

#after
CollisionsSprite((x,y), (w,h), (self.all_sprites, self.collision_sprites))
```

<br>

## 🟡 8.  Link the Player to the Collision Group

### 🔴 Finally, we need to let the player know where all the collision sprites are.

> #### This way, the player can interact properly with the blocks.

#### 🌈 Update the player creation to include the collision group

```python
self.player = Player((400, 300), self.all_sprites, self.collision_sprites)

```


```python
#before
self.player = Player((400, 300), self.all_sprites)

# after
self.player = Player((400, 300), self.all_sprites, self.collision_sprites)
```

## 🔴  But why do we need to do this?

### When the player moves around the game, we want to ensure they can interact with the blocks properly.

> -  #### 🌈 By telling the player about the collision sprites, we enable the game to check if the player is touching or overlapping any of the blocks.

<br>

>#### 🔺  This is essential for the game logic `like stopping the player from walking through walls or detecting when they hit obstacles`.
