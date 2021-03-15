# Introduce Jupyter lab and basic python concepts


## Python, jupyter and scientific programming intro
1. Slides with intro to python and the ecosystem features
    - What about python and scientific programming
        - Why python and the python ecosystem
        - [ ] Go to the Slides showing the python ecosystem
        - Its open source, allows multiple people to contribute
        - Its easy to read
        - It has awesome tools
 
## Hands on    
Executing code in a python interpreter or directly from the command line is useful, but we also want a way to edit and annotate code and go through some process of trial and error when we're solving problems on our own. Anaconda installed JupyterLab, which is a web-based interactive development environment for Jupyter notebooks, code, and data. The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more. ([source](https://jupyter.org/#:~:text=JupyterLab%20is%20a%20web%2Dbased,scientific%20computing%2C%20and%20machine%20learning.))

You can launch Jupyter Lab from your command line from within the folder you want to work in. In this case, we want to create our first Jupyter notebook in the `py_workshop_2021/` folder.

1. Make sure you are in the py_workshop_2021/ folder. If you were in scripts, move up one: `cd ..`
2. Launch Jupyter Lab: `jupyter lab`

You will see a browser window open - this is your local browser, so you will see files in the `py_workshop_2021/` folder there.

1. Move into the `scripts/` folder on the left hand navigation bar.
2. Create a new Jupyter Notebook with a Python 3 kernel by clicking on the icon at the top of the screen.
3. Right click on the new name 'Untitled.ipynb' and select 'Rename' from the list of options. Name it 'day1_exercises.ipynb'

In the Jupyter notebook, the default cell type is code. The convenient thing about working with Jupyter notebooks is you can store text and annotation as important information to go along with your code, so that you or someone else can reproduce it more easily later. Let's start by adding a title and description to this document:

1. Make sure your cursor is in the first cell, then change the type from 'Code' to 'Markdown' at the top menu bar.
2. Click in the cell again, and begin typing. Let's write a title, 'Python Essentials Day 1 Exercises'
3. Hit Shift + Enter to "run" the cell.

1. Markdown is a language with its own syntax for formatting text. Since this is a title, let's make it large and bold:

2. Click back into the first cell
3. Add a # symbol and a space before the title
4. Hit enter twice to create a new line with a space in between
5. Type a short description that will help you remember what this workshop is about. Let it start with: '**Description:**'
6. Hit Shift+Enter to run the cell and see the formatting change.

Now let's work with a code cell to create a simple print statement.

1. In a new cell, check to make sure the type is 'Code' (no need to change anything as that is default)
2. Make a variable called `myname` and assign it a value of your name: `myname = 'Ashley'`
3. Hit enter to get a new line.
4. Create a print statement to say hello using the variable you stored: `print("Hello " + myname + "!")`

You can also write inline annotations to your code to help you remember specific things about what it does. To do this you use the # symbol, in a code cell, Python will not run anything written after the hash symbol per line.

1. Write a short annotation at the end of the line where you store your `myname` variable. `# i got this name at birth :)`
2. Hit Shift+Enter to run the code.

Congratulations, you just wrote and annotated your first Python code in a Jupyter notebook!

## Take aways before going to exerises
- Learning how to program when you are not a computer scientist
    - User scripts
    - Formulate computational problems
    - Understanding how computers work is important
    - Fundamentals are important