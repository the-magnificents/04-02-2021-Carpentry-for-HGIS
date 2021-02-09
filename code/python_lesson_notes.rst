About these instructor notes
============================

Use these notes to run this workshop and guide yourself through
excercises, they are not necessarily meant to be seen by participants,
but it can be helpful for instructors/coinstructors and helpers to
understand what is being taught and the rationale behind teaching this
workshop.

Lets put it as a user story :)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*As an instructor, co-instructor and helper I would like to have some
documented guide on how to teach this workshop and facilitate the
performance of excercises so that I can keep on track of the lesson and
master underlying concepts behind the lesson*

Python scripting and basic data analysis
========================================

Lesson style
------------

These lesson is part of an `open educational
resource <https://en.wikipedia.org/wiki/Open_educational_resources>`__
or module. It is designed to be used in the context of the other
lessons, and builds up knowledge, excercises and concepts using previous
lessons as a foundation.

We start with a program that works, to give a full picture, run first
source code, then inspect the source code, and try to understand it step
by step througout the lesson. The instructor will be reflecting between
essential concepts of python and progressively reviewing the code on the
basis of the new concepts taught. Therefore the instructor will go back
to the source code provided and ask students about specific lines of
code.

Find entire carpentry lesson flow diagram
`here <https://drive.google.com/file/d/1a3gIdHMfKCtgeqvXORqhvfcRrKU4-CAq/view?usp=sharing>`__

|image1|

Checklist
=========

Learning objectives
-------------------

Loading data into Python (geodataframe) - Explore data - Learn how to
work with libraries (for geospatial analysis) - Extrapolate automation
and programming utilities to improve your current workflow - Understand
why this is useful (automation) and advantages over using GIS desktop
apps (or in complement to them)

Take aways (summarizing)
------------------------

-  Practice, explore and be creative
-  Learn from others code
-  Make time to invest in comptuational skills and tools

Technology and setup requirements
---------------------------------

-  What are the requirements to participate in this lesson

Expected outcomes
-----------------

-  By the end of this lesson you will understand fundamental concepts
   underlying python.
-  Practice these concepts through various examples and excercises.

Operations
----------

-  Create the new datasets using the City class manually

What are essential tasks or operations the learner needs to perform in
order to apply the knowledge and concepts? List them Make a basic foor
loop Outcome make a plot

-  Connect bash and commands with setting up ptyhon and also working
   with the file system with python. Introduce basics of data types, the
   philosophy behind python and how to work with libraries. (Carpentries
   material).

-  Run scripts with python (just like we did with bash) and then move to
   jupyter notebooks environments (package management)

Exercises Do a code review example, review some code that does something
you are intersted in.

Lesson notes and materials First just with the python interpreter Then
with jupyter notebooks

Intermediate advanced exercises We can have a list of challenges in the
lesson, for people to try and study other things

Examples Here we can have a list of examples

Errors, reproducing errors….

.. |image1| image:: ./HGIS_carpentries.jpg

Excercise 1: Using someone else’s code
======================================

   Code along (participants repeat what the instructor is doing)

..

   This excercise will help to practice how to use the shell and
   demonstrate where users will navigate directories to find files and
   perform basic operations learned previously.

-  Download the given python repository (our example repository, ideally
   using bash)
-  Explore the python repository only using the terminal(this is a must)

Run the main script of the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Navigate inside the directory and run:
   ``python map.py oregonmap.csv``

Discuss what just happened with the learners in the mindset of
--------------------------------------------------------------

computational thinking - Can anyone explain what might have happened

Excercise 2: Understand someone else’s code (even when you dont know how to program)
====================================================================================

-  Inspect the following code with the learners, ask questions about
   what they are reading.
-  Can you identify roughly which parts of the code are responsible for
   what is happening in the program?
-  What helped you identify the portions of the code?

.. code:: ipython3

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
    # if __name__ == '__main__':
    #     map = Map(sys.argv[1])
    #     map.draw()

Variables (and constants)
=========================

Explain what are variables, and what should the learner know about
variables.

In computer programming, a variable or scalar is a storage location
(identified by a memory address) paired with an associated **symbolic
name**, which contains some known or unknown quantity of information
referred to as a value.

Nice references for instructor
------------------------------

-  `What is a
   Variable? <https://stevenpcurtis.medium.com/what-is-a-variable-3447ac1331b9>`__
-  `Variables
   wikipedia <https://www.google.com/search?q=what+is+a+variable+in+programming&rlz=1C1GCEU_nlNL866NL866&oq=what+is+a+variable+in&aqs=chrome.0.0l3j69i57j0i20i263j0l5.3869j0j1&sourceid=chrome&ie=UTF-8>`__

Data types
----------

-  Strings
-  Numbers (integers and floats)
-  Lists
-  Dictionaries
-  Arrays

Storing different data types
----------------------------

We can use variables to store all sorts of different types of data. We
might be limited by our programming language, but as shown above
Integers, Floats, Characters and Strings are certainly options to be
stored in a variable.

|image1|

Instructor demonstrates these different data types using the python interpreter
-------------------------------------------------------------------------------

.. |image1| image:: https://miro.medium.com/max/875/1*Px7h03Ih7B5QZu4KQpSEoQ.png

.. code:: ipython3

    '''
    Run these commands step by step on the intepreter
    '''
    new_city = City(['c','Havana',-133.996669,190.000000,9500])
    print(new_city.name)


.. parsed-literal::

    Havana
    

Exercises/Operations working with variables
-------------------------------------------

-  Identify with students different data types in the ``map.py`` script.
-  Create variables that represent Delft characteristics as a city.Think
   of characteristics that you can express with different data types
   (integers, strings, arrays)
-  Print formmated data about the city to display these variables in the
   python interpreter.
-  Create a list of cities in the Netherlands. This should be a python
   list containing all cities.

Excercise, exploring objects and data types in the given code
-------------------------------------------------------------

Demonstrate how to work with objects - Create a city object - Inspect a
city object - Modify a city object - Create a map object - Inspect the
list dictionary inside the map object

Instructor needs to know Python Objects and Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   **Why is important to know about objects?** Everything is an object
   in python and most operations done by users involve using
   libraries(objects), using methods and attributes.

..

   Python is an object oriented programming language. Unlike procedure
   oriented programming, where the main emphasis is on functions, object
   oriented programming stresses on objects.An object is simply a
   collection of data (variables) and methods (functions) that act on
   those data. Similarly, a class is a blueprint for that object. We can
   think of class as a sketch (prototype) of a house. It contains all
   the details about the floors, doors, windows etc. Based on these
   descriptions we build the house. House is the object.

.. code:: ipython3

    '''
    These commands are meant to be used first in the python interpreter
    '''
    from map import City
    new_city = City(['c', 'Havana', 0.1, 2.6, 100000])
    print(new_city.name)


.. parsed-literal::

    Havana
    

Go from for loops and while loops to functions
==============================================

   **How to run this section?** Build up the need of using multipline
   commands, to source files, to functions (Demonstrate by example what
   reusability means in this section, this is where functions come into
   place)Reflect on the notion of objects

.. code:: ipython3

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
    
    


.. parsed-literal::

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
    

Knowledge base for instructors (Things I think are interesting and important to understand)
===========================================================================================

What you need to know about python interpreter
----------------------------------------------

Programmer’s view of interpreter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have been coding in Python for sometime, you must have heard
about the interpreter at least a few times. From a programmer’s
perspective, an interpreter is simply a software which executes the
source code line by line.

`How Python
runs <https://indianpythonista.wordpress.com/2018/01/04/how-python-runs/>`__

|image1|

Python is an interpreted programming language. Your Python code actually
gets compiled down to more computer-readable instructions called
bytecode. These instructions get interpreted by a virtual machine when
you run your code.

Have you ever seen a .pyc file or a **pycache** folder? That’s the
bytecode that gets interpreted by the virtual machine.

Run time
--------

In computer science, runtime, run time, or execution time is the final
phase of a computer program’s life cycle, in which the code is being
executed on the computer’s central processing unit (CPU) as machine
code. In other words, “runtime” is the running phase of a program.

Computer memory:
----------------

RAM is the primary or main memory of computer. It is the place where the
text, data, instructions and intermediate results are stored while
executing a program. The total memory is organized into number of bytes
and each byte is again divided into 8 bits.

.. |image1| image:: https://i.imgur.com/c0PRvvI.png
