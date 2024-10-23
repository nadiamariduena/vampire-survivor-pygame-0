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


