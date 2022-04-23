"""
File: score.py
Team No.: 3
Author name: Eduarda (Duda) Reolon
Date completed: 04/18/2022
Description: This program is a class for the score of a snake game.
Testing: The testing for this file was done after the class definition
"""

from turtle import Turtle, Screen
import turtle


class Score:

    def __init__(self, score: int, increment: int):
        """"Create instances from a class definition (__init__) for Score class"""
        
        #On main.py we set initial score to 0
        #Left it open because class can be reused for a game that does not start with 0
        self.score = score 
        self.increment = increment
        self.turtle = Turtle(visible=False) #will be used for text display on turtle screen
        self.turtle.speed('fastest') #text needs to display fast on scren


    def show_score(self, score):
        """ Prints the score board on the top left of the turtle screen """

        #We do not have a title for this game, so score can be put on top with title instead of bottom.
        turtle.title(f"Score: {score}")


    def increment_score(self, score, increment):
        """ Increments score by what programmer wants increment to be """

        score += increment
        return score


    def text_at_xy(self, x, y, text):
        """ Display text on turtle screen """

        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.write(text)

"""
#Coding below tests class
#Brought class into my coding
self = Score(0,10)

# show_score function worked properly
Score.show_score(self,0)

#Defined score variable
score = self.score

# increment_score function worked properly
score = Score.increment_score(self,score,10)
Score.show_score(self,score)

#loop with functions worked properly
while score != 100:
    score = Score.increment_score(self,score,10)
    Score.show_score(self,score)

# text_at_xy function worked properly
if score == 100:
    Score.text_at_xy(self,0,0,"You won!")

turtle.done()
"""
