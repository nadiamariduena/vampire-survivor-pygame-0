## 🟡 Vampire survivor

 <br>
 <br>


## 🟦 Intro

### Following our successful creation of the  ["Space Shooter"](https://github.com/nadiamariduena/python-intro-2024-privat/blob/master/z_PYgame/spaceship_game/RE_game-CODE_17_Debut-game_create_Sounds.md) game in Pygame, we've established a foundational understanding of game development.

> #### Now, we are ready to embark on our second project, which promises to be more immersive and complex.



<br>
<br>
<br>

## 🟠 What We will be doing:

### In this project, we will explore several key concepts essential for building a more sophisticated game.


#### 🍭 Specifically, we will focus on the following four areas:

- - Collision Detection

- - Camera Control

- - Level Creation with an Editor

- - Animation Control


<br>
<br>


#### 🟩 [3:46:05](https://youtu.be/8OMghdHP-zs?si=dvqBnEaPom9xq_-9&t=13565)

🟤 **Collision Detection:** Understanding how to detect collisions between game objects is crucial.

>   #### We will learn various techniques to manage interactions, such as when a player character encounters an enemy or picks up an item.

 This will enhance gameplay by providing feedback and consequences for player actions.

<br>

🟤**Camera Control:** A dynamic camera system can significantly improve the player's experience by providing a better view of the game world.

>   #### We will explore how to implement a camera that follows the player, ensuring that the action remains centered while also allowing for smooth transitions and zooming effects.

<br>

🟤**Level Creation with an Editor:** Building levels manually can be time-consuming and inefficient.

>   #### We'll dive into creating a level editor that allows us to design and modify game environments easily.

>   This will enable us to focus on creativity and gameplay design, making the development process more streamlined.

<br>

🟤**Animation Control:** Proper animation is vital for bringing characters and environments to life.

>   #### We will learn how to manage animations effectively, including creating smooth transitions between different states (e.g., walking, jumping, attacking) and synchronizing them with game  mechanics.


<br>
<br>
<br>
<br>

---

# 🟦 Lets get started

## 🟡 1. Project Setup

**Visit the official page** [code-projects/5games](https://github.com/clear-code-projects/5games) and download the default project folders for the Vampire Game.

#### Once downloaded, add these folders to your **repository**.

<br>

## 🟡 2. Checking Folders

🟤 Before diving into the game development, **take some time to explore each folder** where images are stored.

Here’s what you should look for:

### 🟤 Images Folder:

This folder contains images for the various characters, you will find them inside folders such as: player, enemies, gun.

>#### Each image typically corresponds to different actions or directions, such as:

- down

- left

- down.left

- up

> #### Some images may be ✋ numbered for various animations ( enemies).

<br>

###  🟤 Tiles Folder:

An important folder containing the tile images used for the **game's background** and environment.

<br>

### 🟤 Maps Folder:

Contains the **maps.tmx** file, which stores the game map data.

> ### 🔴 This XML file defines how the game world is structured.


```python
<?xml version="1.0" encoding="UTF-8"?>
<map version="1.10" tiledversion="1.10.1" orientation="orthogonal" renderorder="right-down" width="52" height="50" tilewidth="64" tileheight="64" infinite="0" nextlayerid="5" nextobjectid="175">
 <tileset firstgid="1" source="../tilesets/world_tileset.tsx"/>
 <tileset firstgid="211" source="../tilesets/Objects.tsx"/>
 <layer id="1" name="Ground" width="52" height="50">
  <data encoding="csv">
42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,7,9,42,42,42,7,25,25,25,25,25,9,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,24,25,25,25,26,42,42,42,42,42,24,25,25,9,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,42,42,42,42,42,42,42,24,25,25,9,42,7,25,25,25,25,25,25,25,25,25,25,25,9,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,24,25,26,42,42,42,42,42,42,42,42,42,42,42,24,9,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,14,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,42,42,42,42,42,42,42,34,35,36,42,42,42,42,42,42,1,2,2,3,42,42,42,42,42,24,9,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,1,3,42,42,42,42,34,53,45,46,42,42,42,42,1,2,83,12,12,13,42,42,42,42,42,42,16,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,27,6,42,42,42,42,1,83,13,42,42,42,34,53,42,31,56,42,1,2,82,83,12,12,12,12,13,42,42,42,42,42,42,16,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,16,42,42,42,42,11,12,13,42,42,42,44,45,31,56,42,1,83,12,12,12,12,12,12,61,23,42,42,42,42,42,42,24,9,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,16,42,42,42,42,11,12,13,42,42,42,54,55,56,42,1,61,62,62,63,12,12,12,61,23,42,42,42,42,42,42,42,42,19,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,16,42,42,42,1,83,12,13,42,42,42,42,42,42,42,73,71,72,1,83,12,12,61,23,42,42,42,42,42,42,42,42,42,19,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,16,42,42,42,11,12,12,81,2,3,42,42,42,42,1,83,81,2,83,12,61,22,23,42,42,1,2,3,42,42,42,42,42,16,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,42,16,42,42,42,11,12,12,12,12,81,3,42,42,42,11,12,12,12,12,12,13,42,42,42,42,21,63,81,82,82,3,42,4,29,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,7,26,42,42,1,83,61,22,22,22,22,23,42,42,42,21,62,63,12,12,12,23,42,42,42,42,42,21,63,12,12,13,42,14,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,42,42,42,11,12,13,42,42,42,42,42,42,42,42,42,42,21,22,22,23,42,42,42,42,34,35,36,21,63,12,13,42,14,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,42,42,1,83,61,23,42,42,42,34,35,35,35,35,35,35,36,42,42,42,42,42,42,42,44,45,46,42,11,12,13,42,24,25,25,25,25,25,25,25,25,42,42,
42,42,42,42,42,42,42,42,16,42,42,11,12,13,42,42,42,42,44,45,45,45,45,45,45,46,42,42,42,42,42,42,42,54,55,56,42,11,12,13,42,42,42,42,42,42,42,42,42,42,42,42,
42,42,42,42,42,42,42,42,16,42,42,21,22,23,42,42,42,42,54,55,55,55,32,33,45,46,42,15,4,5,5,6,42,42,42,42,42,11,12,13,42,42,1,2,2,2,2,2,2,2,2,2,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,42,42,42,42,42,42,42,42,44,45,46,42,4,29,42,7,26,42,42,42,42,42,11,12,81,3,42,11,102,12,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,1,2,2,3,42,42,42,42,44,45,46,42,14,15,7,26,42,42,42,42,42,1,83,12,12,81,82,83,102,12,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,73,12,12,12,3,42,42,42,54,55,56,42,14,15,16,42,42,42,42,42,1,12,12,12,12,12,12,94,95,95,95,95,95,95,95,112,112,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,73,12,12,12,12,3,42,42,42,42,42,42,24,25,26,42,42,42,42,42,73,12,12,12,12,12,12,103,12,12,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,21,63,12,12,12,13,42,42,42,42,42,42,42,42,42,42,42,42,42,42,73,12,12,12,12,12,12,103,12,12,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,42,16,42,42,42,34,35,36,42,73,12,12,12,81,3,42,42,42,42,42,42,42,42,42,42,1,2,2,83,12,12,12,12,12,12,103,12,12,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,42,16,42,42,42,44,45,46,42,73,12,12,12,12,81,2,2,3,42,42,42,1,2,2,2,83,12,12,12,12,12,12,12,12,12,103,12,12,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,42,16,42,42,42,54,55,56,42,73,12,12,12,12,12,12,12,81,82,2,2,83,12,12,12,12,12,12,12,12,12,12,12,12,12,103,12,12,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,1,83,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,102,12,12,12,12,12,103,12,12,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,42,16,42,42,42,42,42,42,73,12,12,12,12,12,12,12,12,12,91,92,93,12,12,12,12,12,12,12,102,102,12,12,12,12,12,103,12,102,12,12,12,12,12,12,12,
42,42,42,42,42,42,42,17,26,42,42,42,42,42,1,83,12,12,12,12,12,12,12,12,12,101,102,103,12,12,12,12,12,102,102,102,12,12,12,12,12,12,103,12,102,12,12,12,12,12,12,12,
25,25,25,25,25,25,25,26,42,42,1,2,2,2,83,12,12,12,12,12,12,12,12,12,12,111,112,113,12,12,102,102,102,102,12,12,12,12,12,12,94,95,113,102,102,12,12,12,12,12,12,12,
2,2,2,2,2,2,2,2,2,2,83,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,102,102,102,102,102,12,12,12,12,12,12,12,94,95,113,12,12,12,12,12,12,12,12,12,12,12,
95,95,95,95,95,95,95,95,96,12,12,12,12,12,12,12,12,12,12,12,12,12,102,102,102,102,102,12,12,12,12,12,12,12,12,12,94,95,113,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,101,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,94,95,95,95,113,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,111,96,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,94,112,112,113,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,111,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,113,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,12,12,102,102,102,102,102,102,102,102,102,102,102,102,102,102,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,102,102,102,102,102,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12
</data>
 </layer>
 <objectgroup id="4" name="Entities">
  <object id="38" name="Player" x="1693.33" y="1612">
   <point/>
  </object>
  <object id="39" name="Enemy" x="1734.67" y="946.667">
   <point/>
  </object>
  <object id="40" name="Enemy" x="2093.33" y="782.667">
   <point/>
  </object>
  <object id="41" name="Enemy" x="2556" y="1042.67">
   <point/>
  </object>
  <object id="42" name="Enemy" x="2460" y="1554.67">
   <point/>
  </object>
  <object id="43" name="Enemy" x="2092" y="1152">
   <point/>
  </object>
  <object id="44" name="Enemy" x="1230.67" y="758.667">
   <point/>
  </object>
  <object id="45" name="Enemy" x="1032" y="626.667">
   <point/>
  </object>
  <object id="46" name="Enemy" x="781.333" y="917.333">
   <point/>
  </object>
  <object id="47" name="Enemy" x="953.333" y="752">
   <point/>
  </object>
  <object id="48" name="Enemy" x="730.667" y="1146.67">
   <point/>
  </object>
  <object id="49" name="Enemy" x="694.667" y="1648">
   <point/>
  </object>
  <object id="50" name="Enemy" x="701.333" y="2222.67">
   <point/>
  </object>
  <object id="51" name="Enemy" x="929.333" y="1880">
   <point/>
  </object>
  <object id="52" name="Enemy" x="1068" y="2208">
   <point/>
  </object>
  <object id="53" name="Enemy" x="1380" y="2582.67">
   <point/>
  </object>
  <object id="54" name="Enemy" x="1996" y="2478.67">
   <point/>
  </object>
  <object id="55" name="Enemy" x="1796" y="2181.33">
   <point/>
  </object>
  <object id="56" name="Enemy" x="2266.67" y="2376">
   <point/>
  </object>
  <object id="57" name="Enemy" x="2198.67" y="2102.67">
   <point/>
  </object>
  <object id="58" name="Enemy" x="2557.33" y="2090.67">
   <point/>
  </object>
  <object id="59" name="Enemy" x="2261.33" y="1829.33">
   <point/>
  </object>
  <object id="60" name="Enemy" x="2630.67" y="1706.67">
   <point/>
  </object>
  <object id="61" name="Enemy" x="2381.33" y="1358.67">
   <point/>
  </object>
  <object id="62" name="Enemy" x="684" y="2410.67">
   <point/>
  </object>
  <object id="63" name="Enemy" x="789.333" y="2602.67">
   <point/>
  </object>
  <object id="64" name="Enemy" x="1752" y="2620">
   <point/>
  </object>
  <object id="65" name="Enemy" x="2104" y="2369.33">
   <point/>
  </object>
  <object id="66" name="Enemy" x="2570.67" y="2196">
   <point/>
  </object>
  <object id="67" name="Enemy" x="2432" y="1688">
   <point/>
  </object>
  <object id="68" name="Enemy" x="1986.67" y="1429.33">
   <point/>
  </object>
  <object id="69" x="1064" y="1513.33">
   <point/>
  </object>
  <object id="70" x="1272" y="2018.67">
   <point/>
  </object>
  <object id="71" x="1618.67" y="1912">
   <point/>
  </object>
  <object id="72" x="1473.33" y="1220">
   <point/>
  </object>
  <object id="73" x="1140" y="1122.67">
   <point/>
  </object>
 </objectgroup>
 <objectgroup id="2" name="Collisions">
  <object id="74" x="808" y="1961.33" width="118.667" height="122.667"/>
  <object id="75" x="1605.33" y="2172" width="185.333" height="200"/>
  <object id="76" x="2146.67" y="1378.67" width="128" height="134.667"/>
  <object id="77" x="1321.33" y="925.333" width="129.333" height="134.667"/>
  <object id="78" x="1382.67" y="869.333" width="137.333" height="114.667"/>
  <object id="79" x="1446.67" y="804" width="120" height="133.333"/>
  <object id="80" x="584" y="2625.33" width="1341.33" height="124"/>
  <object id="81" x="1898.67" y="2573.33" width="224" height="90.6667"/>
  <object id="82" x="2081.33" y="2533.33" width="292" height="81.3333"/>
  <object id="83" x="2330.67" y="2453.33" width="174.667" height="102.667"/>
  <object id="84" x="2472" y="2389.33" width="156" height="98.6667"/>
  <object id="85" x="2593.33" y="2338.67" width="188" height="98.6667"/>
  <object id="86" x="2709.33" y="1764" width="489.333" height="613.333"/>
  <object id="87" x="-6.66667" y="2472" width="596" height="240"/>
  <object id="88" x="2626.67" y="1205.33" width="678.667" height="276"/>
  <object id="89" x="2676" y="960" width="178.667" height="357.333"/>
  <object id="90" x="2626.67" y="761.333" width="174.667" height="241.333"/>
  <object id="91" x="2558.67" y="616" width="134.667" height="213.333"/>
  <object id="92" x="1654.67" y="540" width="1050.67" height="110.667"/>
  <object id="93" x="2504" y="630.667" width="113.333" height="64"/>
  <object id="94" x="1586.67" y="550.667" width="210.667" height="158.667"/>
  <object id="95" x="1412" y="500" width="234.667" height="138.667"/>
  <object id="96" x="1217.33" y="433.333" width="305.333" height="150.667"/>
  <object id="97" x="833.333" y="402.667" width="538.667" height="110.667"/>
  <object id="98" x="433.333" y="401.333" width="486.667" height="161.333"/>
  <object id="99" x="336" y="416" width="242.667" height="529.333"/>
  <object id="100" x="521.333" y="857.333" width="118.667" height="506.667"/>
  <object id="101" x="380" y="1274.67" width="185.333" height="1076"/>
  <object id="157" x="1744" y="1606" width="178" height="249"/>
  <object id="158" x="1808" y="1543" width="172" height="177"/>
  <object id="159" x="1942" y="1534" width="104" height="114"/>
  <object id="160" x="1194" y="1448" width="436" height="129"/>
  <object id="161" x="1519" y="1560" width="108" height="188"/>
 </objectgroup>
 <objectgroup id="3" name="Objects">
  <object id="1" gid="218" x="2534.67" y="1940" width="64" height="104"/>
  <object id="2" gid="218" x="1686.66" y="2285.33" width="64" height="104"/>
  <object id="3" gid="218" x="858.667" y="2408" width="64" height="104"/>
  <object id="4" gid="219" x="2505.33" y="2009.33" width="64" height="128"/>
  <object id="5" gid="219" x="2365.33" y="2308" width="64" height="128"/>
  <object id="6" gid="219" x="885.333" y="2500" width="64" height="128"/>
  <object id="7" gid="222" x="1925.33" y="2286.67" width="128" height="192"/>
  <object id="8" gid="222" x="2406.67" y="2833.33" width="128" height="192"/>
  <object id="9" gid="222" x="2753.33" y="2645.33" width="128" height="192"/>
  <object id="10" gid="222" x="2709.33" y="1661.33" width="128" height="192"/>
  <object id="11" gid="223" x="433.333" y="2460" width="128" height="192"/>
  <object id="12" gid="223" x="797.333" y="2461.33" width="128" height="192"/>
  <object id="13" gid="220" x="2718" y="1702" width="60" height="60"/>
  <object id="14" gid="220" x="2822" y="1594" width="60" height="60"/>
  <object id="15" gid="213" x="2242.67" y="1054.67" width="128" height="192"/>
  <object id="16" gid="213" x="762.667" y="685.333" width="128" height="192"/>
  <object id="17" gid="213" x="721.333" y="789.333" width="128" height="192"/>
  <object id="18" gid="215" x="1754.67" y="770.667" width="64" height="128"/>
  <object id="19" gid="215" x="2413.33" y="712" width="64" height="128"/>
  <object id="20" gid="215" x="580" y="1401.33" width="64" height="128"/>
  <object id="21" gid="213" x="1654.67" y="818.667" width="128" height="192"/>
  <object id="22" gid="214" x="2296" y="1132" width="128" height="192"/>
  <object id="23" gid="214" x="1352" y="1672" width="128" height="192"/>
  <object id="24" gid="214" x="1986.67" y="1774.67" width="128" height="192"/>
  <object id="25" gid="214" x="1116" y="1001.33" width="128" height="192"/>
  <object id="26" gid="214" x="1348" y="1400" width="128" height="192"/>
  <object id="27" gid="214" x="553.333" y="2129.33" width="128" height="192"/>
  <object id="28" gid="214" x="598.667" y="1506.67" width="128" height="192"/>
  <object id="29" gid="212" x="768" y="1075.33" width="56" height="60"/>
  <object id="30" gid="212" x="1097.33" y="1043.34" width="56" height="60"/>
  <object id="31" gid="212" x="2228" y="947.333" width="56" height="60"/>
  <object id="32" gid="212" x="2601.33" y="1500.67" width="56" height="60"/>
  <object id="33" gid="212" x="2537.33" y="855.333" width="56" height="60"/>
  <object id="34" gid="211" x="1706" y="1407.33" width="60" height="60"/>
  <object id="35" gid="211" x="1436.67" y="1704.66" width="60" height="60"/>
  <object id="36" gid="211" x="739.333" y="1690" width="60" height="60"/>
  <object id="37" gid="211" x="1263.33" y="1318" width="60" height="60"/>
  <object id="102" gid="222" x="2348.89" y="2902.44" width="128" height="192"/>
  <object id="103" gid="222" x="1738.79" y="2806.2" width="128" height="192"/>
  <object id="104" gid="222" x="2256.09" y="2672.15" width="128" height="192"/>
  <object id="105" gid="222" x="1594.43" y="2333.59" width="128" height="192"/>
  <object id="106" gid="224" x="2021.71" y="2705.46" width="64" height="128"/>
  <object id="107" gid="224" x="2327.61" y="2573.13" width="64" height="128"/>
  <object id="108" gid="224" x="2783.04" y="1847.89" width="64" height="128"/>
  <object id="118" gid="220" x="2810.82" y="1880.91" width="60" height="60"/>
  <object id="119" gid="220" x="2754.1" y="1729.68" width="60" height="60"/>
  <object id="120" gid="221" x="1807.45" y="2827.85" width="56" height="60"/>
  <object id="121" gid="221" x="551.162" y="2515.07" width="56" height="60"/>
  <object id="122" gid="213" x="363.927" y="2204.7" width="128" height="192"/>
  <object id="123" gid="213" x="272.842" y="2120.49" width="128" height="192"/>
  <object id="124" gid="214" x="279.716" y="1668.5" width="128" height="192"/>
  <object id="125" gid="214" x="353.615" y="2092.99" width="128" height="192"/>
  <object id="126" gid="214" x="233.315" y="1909.1" width="128" height="192"/>
  <object id="127" gid="214" x="125.044" y="1355.72" width="128" height="192"/>
  <object id="128" gid="214" x="200.662" y="1006.85" width="128" height="192"/>
  <object id="129" gid="214" x="137.074" y="505.023" width="128" height="192"/>
  <object id="130" gid="214" x="1616.77" y="212.864" width="128" height="192"/>
  <object id="131" gid="214" x="2111.73" y="458.621" width="128" height="192"/>
  <object id="132" gid="214" x="2914.3" y="957.01" width="128" height="192"/>
  <object id="133" gid="214" x="2794" y="1295.57" width="128" height="192"/>
  <object id="134" gid="214" x="3166.93" y="1532.73" width="128" height="192"/>
  <object id="135" gid="215" x="2893.03" y="1313.41" width="64" height="128"/>
  <object id="136" gid="215" x="2722.89" y="698.157" width="64" height="128"/>
  <object id="137" gid="215" x="2195.28" y="364.752" width="64" height="128"/>
  <object id="138" gid="215" x="1667.68" y="402.561" width="64" height="128"/>
  <object id="139" gid="215" x="1128.04" y="266.793" width="64" height="128"/>
  <object id="140" gid="215" x="548.881" y="249.607" width="64" height="128"/>
  <object id="141" gid="215" x="285.938" y="381.938" width="64" height="128"/>
  <object id="142" gid="215" x="378.741" y="897.512" width="64" height="128"/>
  <object id="143" gid="215" x="315.154" y="1088.27" width="64" height="128"/>
  <object id="144" gid="215" x="395.927" y="1342.63" width="64" height="128"/>
  <object id="145" gid="215" x="327.184" y="1511.05" width="64" height="128"/>
  <object id="146" gid="215" x="402.801" y="1767.11" width="64" height="128"/>
  <object id="147" gid="215" x="2061.23" y="1780.86" width="64" height="128"/>
  <object id="148" gid="211" x="2040.89" y="1286.28" width="60" height="60"/>
  <object id="149" gid="212" x="2073.83" y="1324.09" width="56" height="60"/>
  <object id="150" gid="214" x="1882.62" y="1377.84" width="128" height="192"/>
  <object id="151" gid="215" x="1590.34" y="1421.68" width="64" height="128"/>
  <object id="152" gid="215" x="1317.09" y="1287.63" width="64" height="128"/>
  <object id="153" gid="218" x="1853.28" y="1249.85" width="64" height="104"/>
  <object id="154" gid="214" x="1486.67" y="1549.33" width="128" height="192"/>
  <object id="155" gid="215" x="1534.67" y="1626.67" width="64" height="128"/>
  <object id="162" gid="214" x="2190.67" y="1665.33" width="128" height="192"/>
  <object id="163" gid="214" x="1097.33" y="616" width="128" height="192"/>
  <object id="164" gid="214" x="1153.33" y="677.333" width="128" height="192"/>
  <object id="165" gid="213" x="1313.33" y="670.667" width="128" height="192"/>
  <object id="166" gid="215" x="888" y="586.667" width="64" height="128"/>
  <object id="167" gid="215" x="569.333" y="629.333" width="64" height="128"/>
  <object id="168" gid="215" x="693.333" y="826.667" width="64" height="128"/>
  <object id="169" gid="215" x="1120" y="682.667" width="64" height="128"/>
  <object id="170" gid="214" x="2457.33" y="778.667" width="128" height="192"/>
  <object id="171" gid="214" x="2381.33" y="900" width="128" height="192"/>
  <object id="172" gid="214" x="2130.67" y="725.333" width="128" height="192"/>
  <object id="173" gid="214" x="2572" y="1193.33" width="128" height="192"/>
  <object id="174" gid="214" x="705.333" y="1832" width="128" height="192"/>
 </objectgroup>
</map>

```

<br>
<br>

### 🟩 Understanding maps.tmx




#### Here's a breakdown of the key components of the maps.tmx file you provided:

<br>

### 🟢 Basic Structure:

> #### The file begins with the ✋ XML declaration and the `<map>` tag, which specifies



#### Important attributes:



- **version:** Version of the map format.

- **orientation:** Indicates how the map is oriented (e.g., orthogonal).


- **width and height:** Dimensions of the map in terms of tiles (e.g., 52 tiles wide, 50 tiles tall).

- **tilewidth and tileheight:** Size of each tile in pixels (e.g., 64x64 pixels).

<br>

### 🟢 Tilesets:

**`<tileset>` elements specify the images used for the tiles:**

>- - **firstgid:** The first **ID** of the tiles in this tileset, used for referencing them in the map.

- - **source:** The path to the tileset file.

<br>

### 🟢 Layers:



**`<layer>` elements define different layers in the map:**

- - **id:** Unique identifier for the layer.

- - **name:** Name of the layer (e.g., "Ground").

- - **width and height:** Dimensions of the layer in tiles.

- - 🔴 **`<data>:`** Contains the tile **IDs** in CSV format, which correspond to the tiles in the tilesets.

>- - - 🔴 **For example**, a value of 42 might correspond to a specific tile in the tileset.

<br>

### 🟢 Object Groups:

#### `<objectgroup>` contains game entities (like characters and enemies):

- - Each **`<object>`** represents an entity and includes attributes:

- - - **id:** Unique identifier for the object.

- - **name:** Name of the object (e.g., "Player", "Enemy").

- - **x and y:** Coordinates for the object’s position on the map.

<br>

### 🟢 gid (global ID)

the gid (global ID) attribute represents the unique identifier for a tile in the tileset.

- - #### Each tile in a tileset has a global ID that allows the game engine to reference that specific tile when rendering the map.

<br>

### 🟫 Here's a breakdown of how it works:

**Tileset:** A tileset is a collection of tiles (images) that can be used to create the game world. Each tile in this set has a unique ID starting from 1.

**Global ID (gid):**

> - When you see `gid="214"`, it means that this particular tile corresponds to the 214th tile in the tileset being referenced.

- - This ID is used in the map data to specify which tile to draw at each position on the map.

<br>

**Mapping to Tiles:**

-  - In your map, **different areas are defined using these global IDs, so the game knows which tile to render** where based on the IDs listed in the `<data>` section of your layer.

<br>
<br>

## 🟠 Differences

### 🟫 In the context of your `.tmx` file, `id` and gid serve <u>different purposes:</u>

🟤 **id:** This is a unique identifier for the specific object within the context of the layer or the map.

- - **Each object** (like a rectangle, circle, or polygon) in a layer will have its own id, allowing the game engine to reference that particular object.

- - - **This id is usually assigned incrementally** and is used internally for managing the object's properties.

🟤 **gid:** The gid (global ID) specifically refers to the ID of a tile in a tileset.

- - It tells the engine which tile to use when rendering that object.

>In your example, gid="215" indicates that the object is associated with the 215th tile from the tileset.