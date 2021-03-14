
# Instructor Notes: Python Essentials for GIS Learners Day 1 (Unix Shell)
 
This lesson is an introduction to using the Unix shell and the Bash scripting language to create and navigate through files and directories (folders). It is an alternative to \"clicking\" and provides some significant advantages in documenting processes, automating tasks, and enabling reproducible workflows.

The second part of the lesson runs a script called map.py that draws a simple map using the Turtle graphics package. Finally, learners are introduced to Jupyter Lab and using Jupyter notebooks to write and compile code.

The lesson material on Unix Shell is based upon the Software Carpentries lesson on [The Unix Shell](http://swcarpentry.github.io/shell-novice/), the [Introduction to the Command Line for Genomics](https://datacarpentry.org/shell-genomics/) lesson from Data Carpentries, and an [Intro to the Shell](https://datacarpentry.org/2015-11-04-ACUNS/shell-intro/) workshop from softwarecarpentry.org.

The map.py script and oregonmap.csv and californiamap.csv files are from user acleland on GitHub: https://github.com/acleland/turtle-graphics-map distributed and reused under the MIT License.

## Learning goals

The learning goals for this lesson are:
- computers can be used to record and automate iterative tasks
- scripts are a tool for reproducibility
- code is reusable and will consistently produce the same result from the same data file
- code can be used with different data files
- JupyterLab and Jupyter notebooks are important tools for writing and sharing code

## Setup requirements

Participants using Windows OS will need to install Git for Windows following the instructions [here](https://carpentries.github.io/workshop-template/#shell) before Day 1 begins.

The default shell in some versions of macOS is Bash, and Bash is available in all versions, so no need to install anything. You access Bash from the Terminal. The easiest way to find it is by using the magnifying glass symbol at the top right corner of your page and search \"Terminal\". You should open it up and it's a good idea to right click the icon at the bottom of your screen and choose Options > Keep in Dock.

## Data and script for Day 1
Files for the Unix Shell lesson are contained in the `pre_workshop_files/` directory that participants should download and save this folder on their Desktop keeping the name `pre_workshop_files/`.

## Background

The shell is a program that enables us to send commands to the computer and receive output. It is also referred to as the terminal or command line.

Humans and computers commonly interact in many different ways, such as through a keyboard and mouse, touch screen interfaces, or using speech recognition systems. The most widely used way to interact with personal computers is called a graphical user interface (GUI). With a GUI, we give instructions by clicking a mouse and using menu-driven interactions.

While the visual aid of a GUI makes it intuitive to learn, this way of delivering instructions to a computer scales very poorly. Imagine the following task: copying image files one at a time from one location to another. Using a GUI, you would not only be clicking at your desk for several hours, but you could potentially also commit an error in the process of completing this repetitive task. This is where we take advantage of the Unix shell. The Unix shell is both a command-line interface (CLI) and a scripting language, allowing such repetitive tasks to be done automatically and fast. With the proper commands, the shell can repeat tasks with or without some modification as many times as we want. Using the shell, the task in the example can be accomplished in seconds.

The most popular Unix shell is Bash (the Bourne Again SHell — so-called because it’s derived from a shell written by Stephen Bourne). Bash is the default shell on most modern implementations of Unix and in most packages that provide Unix-like tools for Windows.

Using the shell will take some effort and some time to learn. While a GUI presents you with choices to select, CLI choices are not automatically presented to you, so you must learn a few commands like new vocabulary in a language you’re studying. However, unlike a spoken language, a small number of “words” (i.e. commands) gets you a long way, and we’ll cover some of those essentials today.

The grammar of a shell allows you to combine existing tools into powerful pipelines and handle large volumes of data automatically. Sequences of commands can be written into a script, improving the reproducibility of workflows.
The Bash commands, notations and tools taught in this lesson are:

- `cd` - change directory
- `ls` - list (files and directories)
- `ls -F` - list files and directories with a /
- `mkdir` - make directory
- `cat` - show file contents
- `..` - move "up one" directory level
- `mv` - move
- `pwd` - print working directory
- `*` - wildcard used to match filenames
- `>` - used to save output from a command in a file
- `awk` - used for pattern matching and processing


- nano text editor

The Jupyter commands taught in this lesson are:
- `jupyter lab`"

Step 1. Create a new directory and folder structure

### Run your first Bash commands

1. Change Directory to Desktop: `$ cd Desktop
2. List files and directories on Desktop: `my_Desktop $ ls`
3. Try a command error: `my_Desktop $ ks`

### Create the new directories

1. Make a workshop folder called `py_workshop_2021/`: `$ mkdir py_workshop_2021`
2. Change directory to `py_workshop_2021`: `$ cd py_workshop_2021`
3. List contents of `py_workshop_2021/`: `$ ls` (it should be empty)

### Set up the project folder structure

Let's set up a folder structure for our project that is generally useful for any project working with data and code. It's good practice to make separate folders each for raw data, data outputs, scripts and documents in the context of any project you're working on. For now, let's create two new directories, data/ and scripts/ inside the `py_workshop_2021/` directory.

1. Make sure you are in the `py_workshop_2021/` folder: `$ pwd`
2. Create two new directories, `data/` and `scripts/` inside the py_workshop_2021/ folder: `$ mkdir data scripts`

```{admonition} Try on your own
Try creating two new folders for `documentation/` and `demos/` in `py_workshop_2021/`.
```

:::{admonition} Solution
:class: tip, dropdown
`mkdir documentation demos`
::: 

3. Use `ls -F` to verify that your new subdirectories were created.

## Step 2: Move data and script files to the project folder\n",

The data and scripts we want to use are located in the `pre_workshop_files/` folder that we sent out prior to this workshop and you should have saved on your Desktop. Let's take a look at the contents of that folder by navigating there in the shell. If you are in your `py_workshop_2021/` folder, you can use a special notation that means "move up one level": ..

1. Move back to the Desktop and directly into the `pre_workshop_files/` folder: `$ cd ../pre_workshop_files`
2. Use ls to take a look at the files in the `pre_workshop_files/` folder: `$ ls`
3. Take a look at the contents of the documentation.txt file: `$ cat documentation.txt`

### Move files from the `pre_workshop_files/` folder to the `py_workshop_2021/` folder

1. Move `documentation.txt` to `py_workshop_2021/documents`: `$ mv documentation.txt ../py_workshop_2021/documentation`
2. Use `ls` to see that `documentation.txt` is no longer in the `pre_workshop_files/` folder

Note how we use the `../` notation to move one folder "up" from `pre_workshop_files/` to Desktop, and from there we can specify the exact path to the new folder. Note that we didn't actually move there in the terminal - just our files did. 

In `pre_workshop_files/` You should also see a file called `map.py` - this extension lets us know that this is a Python script. We can `cat` into it the same way we did to other files because it is simply a text file with a very particular syntax that Python can read and understand. We don't know much else about it at this moment, and that's ok - let's just move it for now.

```{admonition} Try on your own
Move map.py to the right subfolder within the `py_workshop_2021/` directory.
```

:::{admonition} Solution
:class: tip, dropdown
`$ mv map.py ../py_workshop_2021/scripts`
::: 

### Use wildcards to access multiple files at once

We have three .csv files in the `pre_workshop_files/` folder - `airports_edit.csv`,`netherlandsmap.csv` and `oregonmap.csv`. The last two are both data files that can be run with map.py. We could move each file individually, or type both names in the `mv` command, but there's another way to do this that saves us time.

In Bash, `*` is a wildcard, which matches zero or more characters. Let’s consider the `pre_workshop_files/` directory. `*.csv` matches every file that ends with ‘.csv’. On the other hand, `o*.csv` only matches oregonmap.csv because the ‘o’ at the front only matches filenames that begin with the letter ‘o’. Since we have one file airports_edit.csv that matches the extension but cannot be run with map.py, we want to avoid copying that. How could we do that?

1. You *could* move the two .csv data files from `pre_workshop_files/` to the `data` folder in `py_workshop_2021/`: `$ mv *map.csv ../py_workshop_2021/data`
2. But, we want all the .csv files to go in the data folder. `$ mv *.csv ../py_workshop_2021/data`
    
Now, let's check that everything worked the way we wanted it to. The `pre_workshop_files/` directory should now contain two folders called `mountain_data/` and `qgis/`. Let's move these folders to the `py_workshop_2021/data` and `py_workshop_2021/demos/` directories, respectively.

1. Use `ls` to check that the `pre_workshop_files/` directory is empty as it should be. 
2. Change directory to `py_workshop_2021/`: `cd ../py_workshop_2021`

```{admonition} Try on your own
Check in each of the subdirectories to see if your files are there.
```

:::{admonition} Solution
:class: tip, dropdown
Use `ls -F` to see the subdirectories, then `cd data`, `ls`, `cd ..`;  `cd scripts`, `ls`, `cd ..`; `cd documentation`, `ls`, `cd ..`
::: 

## Step 3: Use nano to add information to the `documentation.txt` file

Nano is a text editor that you can use directly in the command line. Let's add some information about ourselves in the `documentation.txt` file.

1. Move into the `documentation` folder: `cd documentation`
2. Use nano to open the `documentation.txt` file: `nano documentation.txt`
3. Add your name and information about this workshop to that file. Use the arrow keys to navigate and type directly in the editor.
4. Save the changes and write out the file: Control + O; Enter
5. Exit the nano editor: Control + X (you should be back in the terminal)
6. See that your changes were saved: `cat documentation.txt`

## Counting the World's Tallest Mountains

The folder `mountain_data/` has an assortment of files that describe the world's 10 tallest mountains. We are going to demonstrate pipes and pattern matching to count and concatenate files.

1. cd into mountain_data: cd ../data/mountain_data
2. Check out what is there: ls (see mostly text files that follow a naming convention of mountainname-country.txt and two image files)
3. README.md file shows what is there in the dataset
4. cat into one of the files to see it: cat annapurna-np.txt
5. Use pattern matching to list all the files that end with -np.txt: ls *-np.txt
6. Count how many mountains are in Nepal: ls *-np.txt | wc -l

We know there are 10 mountains in this dataset which means that 8/10 of the tallest mountains on earth are in Nepal. 

## Saving the Nepalese tallest mountains in a file (concatenating)

Right now, the data for each mountain are stored in separate files. So we can see the list of mountains in Nepal, but we want one file with all mountains in Nepal. Use the awk command, for pattern processing and matching. The 1 flag automatically inserts a new line between each file.

1. See the list of mountains in Nepal: awk 1 *-np.txt 
2. Save the list using \">\": awk 1 *-np.txt > nepal_mountains.txt
