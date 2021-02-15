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

# City class - contains name, location, and populatin
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

# Allow for command line usage
if __name__ == '__main__':
    # city = City(sys.argv[0])
    map = Map(sys.argv[1])
    map.draw()





