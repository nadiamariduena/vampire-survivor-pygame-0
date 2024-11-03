## 🟡 Vampire survivor

<br>
<br>

## 🟦 Intro

#### [4:33:11](https://youtu.be/8OMghdHP-zs?si=MkVcgh_CaH65GV7K&t=16391)

<br>
<br>

# 🟡 1: Import the Ground Layers

<br>

🟫 **In this step**, we'll continue **expanding the game** world by **importing the ground layers** <u>from our **tile map**</u> .



### 🍏 After successfully adding the trees 🌳, it's time to integrate the rest of the objects, which will enhance the game's environment.

<br>

## 🟤 Importing the Ground  Layer

#### To access the ground layer from your tile map, use the following line of code:


```python
map.get_layer_by_name('Ground')
```

<br>

## 🟤 Adding `.tiles()`

✋ **Next**, we’ll **add `.tiles()` to the line** above to **retrieve the individual tiles** within the ground layer.

 > #### This will allow us to work with each tile's position and image.

```python
map.get_layer_by_name('Ground').tiles()

```


### 🟪 Why Use .tiles()?

**The purpose of `.tiles()`** is **to access the individual tiles** in the **ground layer**.

> 🔴This method **allows us to retrieve not just the layer itself, but also the specific tiles**, making it easier to manipulate them within our game.


<br>
<br>

## `Loop`

## 🟡 2: Using a Loop to Process `Tiles`

- **Now** we need to insert the above line inside a **loop to process each tile.**

```python
for x, y, image in map.get_layer_by_name('Ground').tiles():
```

<br>
<br>

## 🟡 3:  Printing Tile Data

After setting up the loop, let’s print the details of each tile to the console:

```python
for x, y, image in map.get_layer_by_name('Ground').tiles():

    print(x)
    print(y)
    print(image)

```
### 🟠 Expected Output

[4:33:41](https://youtu.be/8OMghdHP-zs?si=Uy4X1dKhCVL5odQt)




- #### 🌈 If you look at the console, you'll see a significant amount of data being generated, which is a positive sign! The next step is to implement sprites that do not trigger collisions.

<br>

>  When you run this code, you’ll see output similar to this in your console:

```python
# This is just a part of all the data I have in the console
43
<Surface(64x64x32)>
30
43
<Surface(64x64x32)>
31
43
```



<br>

<br>

## 🟠 Understanding the Output


### 🟢 `Surface(64x64x32)`:

> #### 🔺 This indicates a tile or sprite surface that is 64 pixels wide, 64 pixels high, and has a depth of 32 bits (often for color depth).

- - - #### 🔺 These <u>indices</u>  are multiplied by 32, which refers to the tile size.



### 🟢 Tile Indices `(30, 31, 43)`:

These numbers represent specific tiles in your tile map.

> - - #### If the numbers represent X and Y positions, you can calculate the pixel positions by multiplying the indices by the tile size (64 pixels).

<br>





## 🟫 Example Calculations

### If you have:

- - 🟤 **Index 30** (assuming this is `X`):

- - - Pixel X Position: **30 * 64 = 1920**

- -  🟤 **Index 43** (assuming this is `Y`):

- - - Pixel Y Position: **43 * 64 = 2752**

### So, if both indices refer to positions in your grid, the pixel coordinates would be (1920, 2752).


<br>
<br>