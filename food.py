"""
File: food.py
Team No.: 3
Author: Michelle Bang
Date completed: 04/21/2022
Description: The food class for the snake game. 
"""

import random
from turtle import Turtle

class Food:

    def __init__(self):

        """ Each attribute of the food class is set to a default value. """
        
        self.food = Turtle() # The food is a turtle.
        self.xpos = 50 # Default x position is at 50.
        self.ypos = 0 # Default y position is at 0.
        self.color = random.choice(['red', 'blue', 'green']) # Color is a random choice between 3 colors.
        self.shape = random.choice(['triangle', 'circle', 'square']) # Shape is a random choice between 3 shapes.
    
    def set_food(self):

        """ Sets the basic features and attributes of the food. """
        
        # All the default attributes are actually implemented to the food turtle.
        food = self.food
        food.speed(0) 
        food.color(self.color)
        food.shape(self.shape)
        food.penup() 
        food.goto(self.xpos, self.ypos)

    def random_location(self, xmin, xmax, ymin, ymax):

        """ Moves the food to a random location. """

        x = random.randint(xmin, xmax) # Random x position is chosen from the two values the user can input.
        y = random.randint(ymin, ymax) # Random y position is chosen from the two values the the user can input.
        
        return self.food.goto(x, y) # Food goes to that random coordinate.

    def track_location(self):

        """ Returns the x, y position of the food. """

        return self.food.pos() 
    
    def hide_food(self):

        """ Hides the food from the screen. """

        self.food.hideturtle()

def main():
    
    """ Testing if the methods work properly."""

    # Setting up the food object.
    food = Food()

    # Applying the attributes to the food.
    movedto = Food.set_food(food)

    # Moving the food to a random location
    randomloc = Food.random_location(food,0,100,0,100)

    # Tracking the location of the food and printing it out.
    print(Food.track_location(food))

if __name__ == "__main__":
    main()


    

    





