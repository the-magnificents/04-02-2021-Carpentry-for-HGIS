# About these instructor notes
Use these notes to run this workshop and guide yourself through excercises, they are not necessarily meant to be seen by participants, but it can be helpful for instructors/coinstructors and helpers to understand what is being taught and the rationale behind teaching this workshop. 

### Lets put it as a user story :) 
*As an instructor, co-instructor and helper I would like to have some documented guide on how to teach this workshop and facilitate the performance of excercises so that I can keep on track of the lesson and master underlying concepts behind the lesson*


# Python scripting and basic data analysis

## Lesson style
These lesson is part of an [open educational resource](https://en.wikipedia.org/wiki/Open_educational_resources) or module. It is designed to be used in the context of the other lessons, and builds up knowledge, excercises and concepts using previous lessons as a foundation.

We start with a program that works, to give a full picture, run first source code, then inspect the source code, and try to understand it step by step througout the lesson. The instructor will be reflecting between essential concepts of python and progressively reviewing the code on the basis of the new concepts taught. Therefore the instructor will go back to the source code provided and ask students about specific lines of code.

Find entire carpentry lesson flow diagram [here](https://drive.google.com/file/d/1a3gIdHMfKCtgeqvXORqhvfcRrKU4-CAq/view?usp=sharing)

![](./HGIS_carpentries.jpg)

## Premises
- We use turtle to show people how to make a minimal GIS data layer programmatically.
- We use pandas and matplotlib to explore datasets

# Checklist

## General learning goals 
- Learn and apply fundamental concepts of python to enhance your computational skills for your own research tasks
- Get inspired and motivated to explore python libraries
- Get exposed to contemporary software tools and basic practices
- Understand the advantages of automation and programmatic operations with CLIs and how they can complement GUI interfaces


## Takeaways from this lesson (summarizing)
- Practice, explore and be creative
- Learn from others code
- Make time to invest in comptuational skills and tools

## Technology and setup requirements
- What are the requirements to participate in this lesson

## Expected outcomes
- By the end of this lesson you will understand fundamental concepts underlying python.
- Practice these concepts through various examples and excercises.

- Connect bash and commands with setting up ptyhon and also working with the file system with python. Introduce basics of data types, the philosophy behind python and how to work with libraries. (Carpentries material).

- Run scripts with python (just like we did with bash) and then move to jupyter notebooks
environments (package management)


Intermediate advanced exercises
We can have a list of challenges in the lesson, for people to try and study other things

Examples
Here we can have a list of examples

Errors, reproducing errors….

## Learning objectives according to the carpentries

### Variables
- Assign values to variables.

### Visualizing tabular data
- Explain what a library is and what libraries are used for.
- Import a Python library and use the functions it contains.
- Read tabular data from a file into a program.
- Select individual values and subsections from data.
- Perform operations on arrays of data.
- Plot simple graphs from data.
- Group several graphs in a single figure.


## Repeating Actions with Loops
- Explain what a for loop does.
- Correctly write for loops to repeat simple calculations.
- Trace changes to a loop variable as the loop runs.
- Trace changes to other variables as they are updated by a for loop.

## Storing Multiple Values in Lists
- Explain what a list is.
- Create and index lists of simple values.
- Change the values of individual elements
- Append values to an existing list
- Reorder and slice list elements
- Create and manipulate nested lists

## Analyzing Data from Multiple Files
- Use a library function to get a list of filenames that match a wildcard pattern.
- Write a for loop to process multiple files.

## Conditionals
- Write conditional statements including if, elif, and else branches.
- Correctly evaluate expressions containing and and or.

## Creating functions
- Define a function that takes parameters.
- Return a value from a function.
- Test and debug a function.
- Set default values for function parameters.
- Explain why we should divide programs into small, single-purpose functions.

## Errors and Exceptions
- To be able to read a traceback, and determine where the error took place and what type it is.
- To be able to describe the types of situations in which syntax errors, indentation errors, name errors, index errors, and missing file errors occur.

## Defensive Programming
- Explain what an assertion is.
- Add assertions that check the program’s state is correct.
- Correctly add precondition and postcondition assertions to functions.
- Explain what test-driven development is, and use it when creating new functions.
- Explain why variables should be initialized using actual data values rather than arbitrary constants.

## Debugging
- Debug code containing an error systematically.
- Identify ways of making code less error-prone and more easily tested.

## Command-Line programs
- Use the values of command-line arguments in a program.
- Handle flags and files separately in a command-line program.
- Read data from standard input in a program so that it can be used in a pipeline.

# Excercise: Using someone else's code
> Code along (participants repeat what the instructor is doing)

> This excercise will help to practice how to use the shell and demonstrate where users will navigate directories to find files and perform basic operations learned previously.

- Download the given python repository (our example repository, ideally using bash)
- Explore the python repository only using the terminal(this is a must)


### Run the main script of the repository
- Navigate inside the directory and run: `python map.py oregonmap.csv`

## Discuss what just happened with the learners in the mindset of 
computational thinking
- Can anyone explain what might have happened

# Excercise: Understand someone else's code (even when you dont know how to program)
- Inspect the following code with the learners, ask questions about what they are reading.
- Can you identify roughly which parts of the code are responsible for what is happening in the program?
- What helped you identify the portions of the code?



```python
# Copyright 2014 Andrew Cleland
# Map drawing using turtle graphics
# Reads data from a csv file to generate a map.

# Import necessary packages
import sys
import csv
from turtle import *

# Global constants
TOWN_MIN = 1   # Min town population
TOWN_MAX = 90000   # Max town population
TOWN_MARK = 2   # radius of town marker
CITY_MARK = 2*TOWN_MARK   # radius of city marker

# City class - contains name, location, and population
class City():
    # Constructor
    def __init__(self, data):
        # data is in form [c, name, x position, y position, population]
        self.name = data[1]
        self.x = float(data[2])
        self.y = float(data[3])
        self.loc = (self.x, self.y)
        self.pop = int(data[4])

# Road class - contains names of connecting cities
class Road():
    # Constructor
    def __init__(self, data):
        # data has form [r, cityname1, cityname2]
        self.city1 = data[1]
        self.city2 = data[2]

# Map class - contains lists of cities and roads
class Map():
    
    # Constructor - generates map from a valid csv file
    def __init__(self, mapfile):
        # Read the file
        map_data = csv.reader(open(mapfile))
        # Initialize city list
        self.cities = {}
        # Initialize road list
        self.roads = []
        # Collect and store data to lists
        for entry in map_data:
            if entry[0] == 'c':
                newCity = City(entry)
                self.cities[newCity.name] = newCity
            elif entry[0] == 'r':
                newRoad = Road(entry)
                self.roads.append(newRoad)
            else:
                print('This shouldn\'t print')

    # Method for drawing the map
    def draw(self):
        
        # Define Screen var - need it for keeping screen open
        scr = Screen()

        # Sub method for drawing labels
        def label(city):
            space = 4   # num pixels to space between marker and label
            penup()
            goto(city.x + space, city.y)
            write(city.name)

        # Make turtle shape an actual turtle
        shape("turtle")

        # Draw cities
        for cityname in self.cities:
            # Load city from cities dictionary
            city = self.cities[cityname]
            # Lift pen, go to location of city
            penup()
            goto(city.x+TOWN_MARK, city.y)
            setheading(90)

            # Draw appropriate marker given population size
            if city.pop > TOWN_MIN and city.pop <= TOWN_MAX:
               pendown()
               circle(TOWN_MARK)
               label(city)
            elif city.pop > TOWN_MAX:
                pendown()
                begin_fill()
                circle(CITY_MARK)
                end_fill()
                label(city)
        
        # Draw roads
        for road in self.roads:
            # Lift pen, go to location of city1
            penup()
            goto(self.cities[road.city1].loc)
            # Apply pen, and go to location of city2
            pendown()
            goto (self.cities[road.city2].loc)
        
        # Remove turtle from the map
        hideturtle()

        # Keep screen open until user closes it
        scr.mainloop()

# # Allow for command line usage
if __name__ == '__main__':
    map = Map(sys.argv[1])
    map.draw()
```

# Variables (and constants)
Explain what are variables, and what should the learner know about variables.

In computer programming, a variable or scalar is a storage location (identified by a memory address) paired with an associated **symbolic name**, which contains some known or unknown quantity of information referred to as a value.

## Nice references for instructor
- [What is a Variable?](https://stevenpcurtis.medium.com/what-is-a-variable-3447ac1331b9)
- [Variables wikipedia](https://www.google.com/search?q=what+is+a+variable+in+programming&rlz=1C1GCEU_nlNL866NL866&oq=what+is+a+variable+in&aqs=chrome.0.0l3j69i57j0i20i263j0l5.3869j0j1&sourceid=chrome&ie=UTF-8)




## Exercise, working with variables
- Identify with students different data types in the `map.py` script.
- Create variables that represent Delft characteristics as a city.Think of characteristics that you can express with different data types (integers, strings, arrays)
- Print formmated data about the city to display these variables in the python interpreter.
- Create a list of cities in the Netherlands. 
    This should be a python list containing all cities.

- print user friendly outputs with the print function


##  Data types
- Strings
- Numbers (integers and floats)
- Lists
- Dictionaries
- Objects

## Storing different data types
We can use variables to store all sorts of different types of data.
We might be limited by our programming language, but as shown above Integers, Floats, Characters and Strings are certainly options to be stored in a variable.

![](https://miro.medium.com/max/875/1*Px7h03Ih7B5QZu4KQpSEoQ.png)
 
## Instructor demonstrates these different data types using the python interpreter


```python
'''
Run these commands step by step on the intepreter
'''
new_city = City(['c','Havana',-133.996669,190.000000,9500])
## check types (no need to use print in the python shell)
print(type(new_city))

## Explain the object stored in memory
print(new_city)
## Print a property of the city
print(new_city.name)
```

    <class '__main__.City'>
    <__main__.City object at 0x000002696DC80D90>
    Havana
    

## Excercise, exploring objects and data types in the given code
Demonstrate how to work with objects
- Create a city object from the given class
- Inspect the city object created
- Modify a city object
- Create a map object
- Inspect the dictionary inside the map object


### For this exercise the instructor needs to know Python Objects and Classes
> **Why is important to know about objects?** Everything is an object in python and most operations done by users involve using libraries(objects), using methods and attributes.

> Python is an object oriented programming language. Unlike procedure oriented programming, where the main emphasis is on functions, object oriented programming stresses on objects.An object is simply a collection of data (variables) and methods (functions) that act on those data. Similarly, a class is a blueprint for that object. We can think of class as a sketch (prototype) of a house. It contains all the details about the floors, doors, windows etc. Based on these descriptions we build the house. House is the object.



```python
'''
These commands are meant to be used first in the python interpreter
'''
## Skip first this step and look at the error
from map import City

# 1. Skip this step and only doing after reflecting on error
# from map import Map

# 2. Create a city object from the given class
new_city = City(['c', 'Havana', 0.1, 2.6, 100000])

## 3. Inspect a city object
print(new_city.name)

## Create a map object
new_map = Map('oregonmap.csv')

## Inspect the Map 
```

    Havana
    

# Go from for loops and while loops to functions
> **The main idea behind this section**. Reusing instructions (programmatic operations and instructions, storing instruction on files(scripts), and reusing functions)

> **How to run this section?** Build up the need of using multipline commands, to source files, to functions (Demonstrate by example what reusability means in this section, this is where functions come into place)Reflect on the notion of objects

In order to work with python built in IDLE do `py -3 -m idlelib`


## Excercise, drawing polygons with turtle
This excercise also aims to show the 


```python
import turtle
## Explain differences
# from turtle import * 

## Explain how to use the help()
# help(turtle)

## Excercise: 
# Do this first manually
# turtle.shape("turtle")
# turtle.forward(100)
# turtle.setheading(90)
# turtle.forward(100)
# turtle.setheading(180)
# turtle.forward(100)
# turtle.setheading(270)
# turtle.forward(100)

## Do it then with a for loop
## Explain the need for a foor loop
# length = 100
# directions = [0,90,180,270]
# for dir in directions:
#     turtle.setheading(dir)
#     turtle.forward(length)

## Example of a function
## triangle = [[a_side, C_angle], [b_side, A_angle], [c_side, B_angle]]
def draw_triangle(triangle):
    for entry in triangle:
        print(entry[0])
        turtle.forward(entry[0])
        turtle.left(entry[1])

## Excercise: 
## Building a polygon with a better data model
def draw_polygon(coordinates):
    '''
    By doing myself this excercise I figured out problems to solve
    like for instance the if statement at the end of the function
    '''
    turtle.penup()
    count = 0
    for coord in coordinates:
        count += 1 
        turtle.goto(coord[0], coord[1])
        turtle.pendown()
        turtle.circle(5)
        # turtle.penup()
        if(count == len(coordinates)):
            turtle.goto(coordinates[0][0], coordinates[0][1])

## Another triangle data model
## A polygon model
##   Latitude,Longitude
##   [[51.984338,4.136685],
##   [51.852919,5.290831],
##   [52.861383,5.024489]]

## Explain this example first and why is it so bad
# draw_triangle([[100,100],[264,19],[300,60]])
# draw_triangle([[100,100],[264,180-19],[300,60]])

## Explain these example and the data model and why is better.
# draw_polygon([[20,30],[100,200],[-50,180]])
# draw_polygon([[20,30],[100,200],[-50,180],[300,-150]])

turtle.exitonclick()

```


    ---------------------------------------------------------------------------

    Terminator                                Traceback (most recent call last)

    <ipython-input-25-892a727f1ebd> in <module>
         63 # draw_polygon([[20,30],[100,200],[-50,180],[300,-150]])
         64 
    ---> 65 turtle.exitonclick()
    

    ~\Anaconda3\lib\turtle.py in exitonclick()
    

    Terminator: 


## Excercise, combining functions and object orientation 
- Calculate the total population in the dataset
- Calculate the biggest city in the dataset
- Make a script file with a function where you calculate to reuse this calculation.


```python
import map
new_map = map.Map('oregonmap.csv')

# print(new_map.cities)
# Then invite students to reflect what the number means, city object at0x000123....
# Rep: print a specific city in delft new_map.cities[<SELECTED CITY>]

# Invite students to do a for loop
for city in new_map.cities:
    print(city)      # THIS IS JUST PRINTING THE KEY
    # print(city.name) # EXPLAIN WHY THIS GIVES AN ERROR
    # print(new_map.cities[city])
    # print(new_map.cities[city].name, new_map.cities[city].pop)


```

    Astoria
    Portland
    Salem
    Corvallis
    Eugene
    _1
    Coos Bay
    _3
    Newport
    Reedsport
    Lincoln City
    Klamath Falls
    Bend
    _2
    The Dalles
    Pendleton
    Burns
    Lakeview
    Medford
    

# Knowledge base for instructors (Things I think are interesting and important to understand)

## What you need to know about python interpreter
### Programmer’s view of interpreter
If you have been coding in Python for sometime, you must have heard about the interpreter  at least a few times. From a programmer’s perspective, an interpreter is simply a software which executes the source code line by line.

[How Python runs](https://indianpythonista.wordpress.com/2018/01/04/how-python-runs/)

![](https://i.imgur.com/c0PRvvI.png)

Python is an interpreted programming language. Your Python code actually gets compiled down to more computer-readable instructions called bytecode. These instructions get interpreted by a virtual machine when you run your code.

Have you ever seen a .pyc file or a __pycache__ folder? That’s the bytecode that gets interpreted by the virtual machine.

## Run time
In computer science, runtime, run time, or execution time is the final phase of a computer program's life cycle, in which the code is being executed on the computer's central processing unit (CPU) as machine code. In other words, "runtime" is the running phase of a program.

## Computer memory:
RAM is the primary or main memory of computer. It is the place where the text, data, instructions and intermediate results are stored while executing a program. The total memory is organized into number of bytes and each byte is again divided into 8 bits.

