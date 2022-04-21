"""
File: main.py
Team No.: 3
Author name: Fernando Salazar, Michelle Bang, and Eduarda (Duda) Reolon
Date completed: 04/21/2022
Description: This program is the main code for a snake game that imports the classes Food, Snake and Score.
"""
import turtle

from snake import Snake
from snake import SnakeCollision
from turtle import Screen, Turtle
import time
from food import Food
from score import Score


def options(lost):
    # create buttons
    button_yes = Turtle()
    button_yes.hideturtle()

    button_yes.penup()
    button_yes.goto(0, 0)

    if lost == 0:
        button_yes.write("  You have Lost click on screen to Play again!!", align="center",
                         font=("arial", 15, "normal"))
    else:
        button_yes.write("  You have Won click on screen to Play again!!", align="center",
                         font=("arial", 15, "normal"))

    def screenclick(x, y):
        if -300 < x < 300 and -300 < y < 300:
            button_yes.clear()
            snake_game()

    turtle.onscreenclick(screenclick, 1)
    turtle.listen()


def snake_game():
    # setup main window
    main_screen = Screen()
    main_screen.setup(width=500, height=500)
    main_screen.bgcolor("white")
    main_screen.tracer(0)

    # Create score
    self = Score(0, 10)
    Score.show_score(self, 0)
    score = self.score

    # creates the snake object
    viper_attributes = Snake()
    viper_head = viper_attributes.snake_creation()

    # creates the snake body object
    viper_body = viper_attributes.snake_body_creation()

    # Michelles code
    # Setting up the food object.
    food = Food()

    # Applying the attributes to the food.
    movedto = Food.set_food(food)

    # binds keys
    main_screen.listen()
    main_screen.onkey(viper_attributes.up, "Up")
    main_screen.onkey(viper_attributes.down, "Down")
    main_screen.onkey(viper_attributes.right, "Right")
    main_screen.onkey(viper_attributes.left, "Left")

    # main game loop
    while True:

        # sets the new x and y cor
        viper_head.setx(viper_attributes.prep_move_x(viper_attributes.direction, viper_head.xcor()))
        viper_head.sety(viper_attributes.prep_move_y(viper_attributes.direction, viper_head.ycor()))

        # screen update
        main_screen.update()

        # Checks for collision into wall
        collision = SnakeCollision(viper_head.xcor(), viper_head.ycor(), len(viper_body), viper_body, viper_head)
        if collision.wall_collision():
            main_screen.clear()
            viper_attributes.clear_body()
            food.hide_food()
            # Score.text_at_xy(self, 0, 0, "You lost!")
            # Score.text_at_xy(self, 0, -50, "Click to play it again")
            options(0)
        # checks for collision into self
        if collision.self_collision():
            main_screen.clear()
            viper_attributes.clear_body()
            food.hide_food()

            Score.text_at_xy(self, 0, 0, "You lost!")
            Score.text_at_xy(self, 0, -50, "Click to play it again")
            options(0)

        # moves the snake body sections around
        viper_attributes.move_body_sections(viper_body, viper_head)

        # Moving the food to a random location
        if viper_head.distance(food.track_location()) < 20:
            Food.random_location(food, -220, 220, -220, 220)
            # creates the snake body object
            viper_body = viper_attributes.snake_body_creation()
            # moves new body correct location
            viper_attributes.move_body_sections(viper_body, viper_head)
            # score updating
            score = Score.increment_score(self, score, 10)
            Score.show_score(self, score)

        # winning
        if score == 1000:
            main_screen.clear()
            viper_attributes.clear_body()
            food.hide_food()
            # Score.text_at_xy(self, 0, 0, "You won!")
            # Score.text_at_xy(self, 0, -50, "Click to play it again")
            options(1)
        # delayed used to slow down game
        delay = 0.1
        time.sleep(delay)


def play_again():
    snake_game()


if __name__ == '__main__':
    snake_game()
