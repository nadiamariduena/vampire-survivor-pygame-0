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
