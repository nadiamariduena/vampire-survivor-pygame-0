## 🟡 Vampire survivor


<br>
<br>


## 🟦 Intro





#### [3:55:55](https://youtu.be/8OMghdHP-zs?si=EaQXjYMwheIf3E4p&t=14155)

<br>



## 🫐   Player <u>Movement</u>  Implementation




## 🟡  1.  Let's Add Input and Movement

### Now, we need to focus on two important things:

- - **input** (handling the player's actions) and

- - **movement** (moving the player around).


#### These will be part of the player's update process.

<br>

```python
    def input(self):
        pass  # Here we will handle player controls (like keyboard input)

    def move(self, dt):
        pass  # Here we will move the player based on input

```

### These two methods will be called inside the `update()` method, which runs every frame to keep everything updated:

```python
    def update(self, dt):
        self.input()  # Get player input (e.g., keyboard presses)
        self.move(dt)  # Move the player based on input

```

>This way, the player’s input and movement are checked and updated every frame!




<br>
<br>

## 🟡  2. Defining the Player's Position and Movement Direction

We will be adding this 3 lines to the Player class

```python
     self.rect = self.image.get_frect(center = pos)
     self.direction = pygame.Vector2(1,0)
     self.speed = 500
     self.rect.center += self.direction * self.speed * dt
```

### `self.rect = self.image.get_frect(center=pos)`

 #### 🟢 This line creates a rectangle around our character’s image, helping Pygame know exactly where our player is on the screen.

>  #### The *`center=pos`* part means we’re placing that **square** right where we want our player to start.

#### Think of it as putting our character in their perfect starting position!



### `self.direction = pygame.Vector2(1, 0)`

####  Here, we’re defining which way our player is facing.

> #### 🌈 A Vector2(1, 0) means the player is pointed to the right.

> If we wanted them to look up or down, we could change this to something like **Vector2(0, -1)** or **Vector2(0, 1)**.

This simple line provides our character with a clear path to follow (like a reliable compass)!

<br>

## 🟤 The Movement Magic 🌟

- In the **move** method, we see this line:

```python
self.rect.center += self.direction * self.speed * dt
```


<br>


## 🟤 Add it to the code

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("../images", "player", "down", "0.png" )).convert_alpha()

        self.rect = self.image.get_frect(center = pos)


    # MOVEMENT
        self.direction = pygame.Vector2(1,0) # A Vector2(1, 0) means the player is pointed to the right.


        self.speed = 500
        # The speed is set to 500, which means the character moves quite quickly.


    def input(self):
        pass

    def move(self,dt):
        self.rect.center += self.direction * self.speed * dt
The speed is set to 500, which means the character moves quite quickly.
    def update(self, dt):
        self.input()
        self.move(dt)
```

### Output

#### 🔴 We have some movement but we can see the last frame

[<img src="setup_player_game_01_moving-the-player.png"/>]()



<br>

## 🫐 Motion blur type

You will see your character is zipping to the right, and that shadow you’re seeing behind the character looks like **"motion blur"** or a trail effect.

<br>

🟤 **Explanation 1:** So, when you see your character running to the right with a sort of shadow behind them, <u>it’s because as the player moves, the previous positions linger for just a moment before disappearing</u> .

> This creates that cool trailing effect, making it look like they’re zooming by just like a comet leaving a trail in the sky! 🌠

<br>



🟤 **Explanation 2:** As your player moves, it’s using a series of images (frames) to show movement.

-  - **Each frame is a snapshot of the character in different positions**.

> - When the game runs, it draws these frames quickly, creating the illusion that your character is gliding smoothly.

<br>

#### Imagine a `flipbook`, if you flip through the pages fast enough, it looks like the pictures are moving!

<br>

[<img src="setup_player_game_01_moving-the-player.gif"/>]()

<br>
<br>

## 🌈 Solution

- Go to the Game class within the main.py

- add this line: `self.display_surface.fill("black")`

 <br>

```python
        # -- DRAW --
            # Draw the current frame to the display
            self.display_surface.fill("black") # ✋
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()

        # Quit all pygame modules when the game loop ends
        pygame.quit()
```

 <br>

[<img src="setup_player_game_02_moving-the-player_removing_last-frame.gif"/>]()


<br>
<br>

## 🟦 Before moving on

### 🟠 Remove the values within the vector (we only need it to test the char movements)

```python
# BEFORE
self.direction = pygame.Vector2(1,0) # A Vector2(1, 0) means the player is pointed to the right.

# AFTER
self.direction = pygame.Vector2() # A Vector2(1, 0) means the player is pointed to the right.
```