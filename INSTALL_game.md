## 🟡 Environment creation

- Each game project will have different modules to install

<br>
<br>

#### 1. Within your /Project folder, create:

- -  `.gitignore` file, add this: **.myvenv**



#### 2. Within your /Project folder, create:

- - `test.py` (or whatever you want to call it)

#### 3. Within your /Project folder, Create the Environment:

🌈 **In your terminal:** Check if you are in your **/Project** (this is important) because I am going to install some modules (I only want them installed in that specific project)

<br>

 - - CREATE the **environment:** Type this in your project terminal `python -m venv .myvenv`

 <br>

- - ACTIVATE the **environment:** Type this in your project terminal `source .myvenv/bin/activate`

<br>

#### 4. Verify activation:

>Once ACTIVATED (you should see the `(.venv)mycomputer@usercomp:~/YOURPROJECT/`) , if you dont see the venv its not activated.

<br>
<br>

### 🔴 Remember that the modules you install in each project is different

<br>

#### 5. 🧶 Install Modules: PYGAME:

#### Check this:  [min 6:18  | Master Python by making 5 games [the new ultimate introduction to pygame]](https://youtu.be/8OMghdHP-zs?si=7R42dHMCVIj3YqG9&t=378)

<br>

- - INSTALL this:   `pip install pygame`

- - Then Install:  `pip install pygame-ce`
`


<br>

- After installing your first module, generate the `requirements.txt` file to see the packages you've installed. This is different from **pip list**, which displays the installed modules in the terminal but does not create a file.

```python
# type this to generate the requirements.txt
pip freeze > requirements.txt

```



<br>
<br>

#### 6. VERIFY the installation

- - VERIFY the installation: Type this in your project terminal `pip list`

```bash

Package            Version
------------------ --------
certifi            2024.7.4
charset-normalizer 3.3.2
idna               3.7
pip                22.0.4
pygame             1.6.0 ✋
requests           1.31.0 ✋
setuptools         47.1.0
urllib3            2.0.7
```