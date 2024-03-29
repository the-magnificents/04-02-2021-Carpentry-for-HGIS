# Instructor Notes: Python Essentials for GIS Learners Day 3

This lesson is focused on understanding and implementing version control with Git and remote collaboration in GitHub on a code-based project. We'll talk about the utility of version control systems for tracking changes to local projects, and how it can be used to enable remote collaboration and crediting of multiple authors to a project hosted in a remote repository like GitHub. This material draws from the [Version Control with Git](https://swcarpentry.github.io/git-novice/) lesson from the Software Carpentries. 

This lesson uses the Gizmo repository (https://github.com/wmvanvliet/gizmo) from wmvanvliet on GitHub as a basis for Python challenges and to illustrate a track changes workflow. 

About the repository: "This is a Python challenge. Create pull requests (PR's) to this repository to solve it. Upon PR submission, the GitHub action robots will check your code and report back how well you did. You can then add more commits to your PR until all tests come back green, which means you win! (*note:* you can also do all exercises locally and run the test to check if you pass or fail each exercise, without needing to do a pull request. This is how we will do it in this lesson.) The exercises are meant to test your knowledge of some important features of the Python programming language and the NumPy and Pandas libraries. When it's not immediately obvious to you how to solve an exercise using only a few lines of code, it is likely you can learn a new Python trick by checking the links below the exercise."

## Learning goals

The learning goals for this lesson are:
- tracking changes with Git
- contributing and collaborating with others in remote repositories

## Setup requirements

For Windows users, Git should be installed already as part of the Bash install from Day 1. 

Mac users need to install Git for Mac by downloading and running the most recent "mavericks" installer from [this list on Sourceforge.net](https://sourceforge.net/projects/git-osx-installer/files/). Because this installer is not signed by the developer, you may have to right click (control click) on the .pkg file, click Open, and click Open on the pop up window. After installing Git, there will not be anything in your /Applications folder, as Git is a command line program. 

More detailed instructions and videos are available here: https://carpentries.github.io/workshop-template/#git

## Data and code for this lesson

The material for this lesson is found in the Gizmo Python Challenges repository by wmvanvliet on GitHub. Participants do not need to do anything ahead of the lesson as the first part walks them through forking and cloning a repository on GitHub. The link is here: https://github.com/wmvanvliet/gizmo

## Background

Version control is the lab notebook of the digital world: it’s what professionals use to keep track of what they’ve done and to collaborate with other people. Every large software development project relies on it, and most programmers use it for their small jobs as well. And it isn’t just for software code: books, papers, small data sets, and anything that changes over time or needs to be shared can and should be stored in a version control system.

A version control system is a tool that keeps track of these changes for us, effectively creating different versions of our files. It allows us to decide which changes will be made to the next version (each record of these changes is called a commit), and keeps useful metadata about them. The complete history of commits for a particular project and their metadata make up a repository. Repositories can be kept in sync across different computers, facilitating collaboration among different people. Version control systems start with a base version of the document and then record changes you make each step of the way. You can think of it as a recording of your progress: you can rewind to start at the base document and play back each change you made, eventually arriving at your more recent version.

## Remote collaboration

Collaborative writing or scripting with traditional word processors and text editors is cumbersome. Either every collaborator has to work on a document sequentially (slowing down the process of writing), or you have to send out a version to all collaborators and manually merge their comments into your document. The ‘track changes’ or ‘record changes’ option can highlight changes for you and simplifies merging, but as soon as you accept changes you will lose their history. You will then no longer know who suggested that change, why it was suggested, or when it was merged into the rest of the document. 

Some word processors let us deal with this a little better, such as Microsoft Word’s Track Changes, Google Docs’ version history, but they lack a streamlined way to customise messages about changes made and store just one latest version of the file for everyone working on it. It seems ridiculous to have multiple nearly-identical versions of the same document that we keep passing back and forth to create something whole. The result is a lot of files with names like Final_paper_EDIT01.doc or Final_paper_EDITCOMMITTEE03.doc and so on...it can get messy trying to merge suggestions and changes made by multiple people in multiple documents, sent over email...I'm sure we all know the headache!

When using a remote collaboration like Git Hub, unless multiple users make changes to the same section of the document - a conflict - you can incorporate two sets of changes into the same base document.

From [GitHub Guides](https://guides.github.com/activities/hello-world/): "GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere." GitHub hosts code and all files for each project in a **repository**, sometimes shortened to "repo". A repository on GitHub is free to create, you can add contributing members and collaborators with different permission settings as you please, and you can access it with a unique URL.

## Individual work
Teams are not the only ones to benefit from version control: lone researchers can benefit immensely. Keeping a record of what was changed, when, and why is extremely useful for all researchers if they ever need to come back to the project later on (e.g., a year later, when memory has faded).

## Step 1: Set up Git configuration settings

1. Open up your terminal or GitBash command prompt to configure your Git global settings:
2. Your name: `$ git config --global user.name "<insert your name here>"`
3. Your email address: `$ git config --global user.email "<insert your email here>"` **should be the same as the one used when setting up your GitHub account.**
4. Your preferred text editor: `$ git config --global core.editor "nano -w"`
5. Check your settings: `$ git config --list`

## Step 2: Fork the [Gizmo Python challenges repository](https://github.com/aecryan/gizmo) on GitHub

1. Sign into your account on GitHub
2. Go to this repository url: https://github.com/aecryan/gizmo
2. On the top right of the repository, find the small gray button that says "Fork". Click this button to fork the repository (create a copy) in your own account.

## Step 3: Clone the forked copy of the Gizmo Python challenges repository to your local computer

1. Click the green button near the top of the screen that says "Code". We will use HTTPS to connect between the remote repository and our local machine.
2. Copy the link under HTTPS heading 
3. In your terminal/command prompt change directory to your Desktop: `cd Desktop`
4. Clone the repository to your Desktop: `git clone https://github.com/aecryan/gizmo.git`. You will see a new folder appear on your desktop called "gizmo". 

### Explore .git folder and local git repo

1. Enter the new repository folder: `cd gizmo`
2. Check out its contents including hidden files/directories: `ls -a`
3. Notice the . git folder which contains all the information that is necessary for your project in version control and all the information about commits, remote repository address, etc.
4. See how Git stores your credentials that were set up earlier: `cd .git` , `cat config`. 
5. Move back to the main gizmo folder: `cd ..` 
6. Check the files that are in the gizmo directory: `ls` There are two files, README.md and titanic.csv. These are the same files as are on GitHub. There is also a .gitignore file. 
7. See the remote connection: `git remote -v` If you ever forget a command, or need help, you can use `git config -h` for a list of commands and `git config --help` to access the detailed Git manual.

## Step 4: Create a new branch and gizmo.py file

### Make a new branch 

1. Create a new branch and give it your name: `git checkout -b <yourname>`. You will get a message: Switched to a new branch 'yourname'
2. Check which branch you are on: `git branch`. You will see two branches, master and the one you named, which should be highlighted and have a little asterisk next to it. 
3. See that the same files are in this new branch: `ls` (README.md and titanic.csv).

### Make a new file called gizmo.py (a python script) and try Python challenge 2
1. Create a new file called gizmo.py: `nano gizmo.py`. This will create and enter the editor in one step.
2. Define a function that takes two arguments, name and country, and prints the message, Hello '<name>', how are things in '<country>'? The country should default to Finland (see Exercise 2 from Gizmo Python challenges repository).

:::{admonition} Solution
:class: tip, dropdown
```python
def hello(name, country='Finland'):
  print("Hello "+ name + ","+" how are things in "+ country + "?"))
  ```
:::

3. Open your Python intepreter: in Mac, type `python` in terminal
4. Import the new gizmo module you just created: `import gizmo` 
5. Print a custom message by running: `gizmo.hello('Your Name', 'Your Country')`

## Step 5: Add and commit changes to local git repository

1. Check that git has noticed new gizmo.py file: `git status`
2. Add gizmo.py to the staging area: `git add gizmo.py`
3. Check that git has added gizmo.py to staging area: `git status`
4. Commit the new file to git's history: `git commit -m "defined hello function in gizmo.py"`
5. Check that the commit has been made: `git status`

## Step 6: Push changes to remote repository in GitHub

1. Try `git push` - error message because there is no branch in the remote repository called 'yourname' 
2. Copy and paste the suggested command: `git push --set-upstream origin <yourname>` - message: 'Branch 'yourname' set up to track remote branch <yourname> from origin'
3. Check to see if changes were pushed successfully: `git status`
4. Check on GitHub to see that changes were successfully pushed. Click on branches drop down menu and show all, select 'yourname', here you should see a new file called gizmo.py which contains the "hello" function you defined.

## Step 7: Test your answers to Python challenges

1. Run the test_gizmo.py script which tests the answers you try for each Python challenge: `python -m pytest .tests/test_gizmo.py`. This should show a list of tests two to fourteen and pass/fail for each one. At the top there is a list of fourteen characters, if you pass a test it will show a green dot, if you fail it there should be a red F.   
2. Try the rest of the exercises (3-12) on your own, running the same command after each one.
3. If you need to change something about your answer to make it pass, use: `nano gizmo.py` and make your changes. Don't forget to track and commit changes with Git :)