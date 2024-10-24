
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

