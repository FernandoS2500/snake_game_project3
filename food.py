"""
File: food.py
Team No.: 3
Author: Michelle Bang
Date completed: 04/17/2022
Description: The food class for the snake game. 
"""

import random
from turtle import Turtle

class Food:

    food = Turtle()
    color = random.choice(['red', 'blue', 'green'])
    ypos = 0
    xpos = 50
    shape = random.choice(['triangle', 'square', 'circle'])

    def __init__(self, food, xpos, ypos, color, shape):

        """ Each attribute of the food class is set to a default value. """
        
        food = food
        xpos = xpos
        ypos = ypos
        color = color
        shape = shape
    
    def set_food(self):

        """ Sets the basic features and attributes of the food. """

        food = self.food
        food.speed(0)
        food.color(self.color)
        food.shape(self.shape)
        food.penup()
        food.goto(self.xpos, self.ypos)

    def random_location(self, xmin, xmax, ymin, ymax):

        """ Moves the food to a random location. """

        x = random.randint(xmin, xmax)
        y = random.randint(ymin, ymax)
        
        return self.food.goto(x, y)

    def track_location(self):

        """ Returns the x, y position of the food. """

        return self.food.pos()


def main():
    
    """ Testing if the methods work properly."""

    # Setting up the food object.
    food = Food(Turtle(), 0, 50, "red", "circle")

    # Applying the attributes to the food.
    movedto = Food.set_food(food)

    # Moving the food to a random location
    randomloc = Food.random_location(food,0,100,0,100)

    # Tracking the location of the food and printing it out.
    Food.track_location(food)

if __name__ == "__main__":
    main()


    

    





