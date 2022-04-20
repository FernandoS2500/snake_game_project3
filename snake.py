"""
File: snake.py
 Team No.: 03
 Author name: Fernando Salazar
 Date completed: 04/17/2022
 Description:  The snake.py file has two classes Snake and SnakeCollision. Snake allows the
 software to create a snake using turtle and move it around. SnakeCollision checks if the snake has
 run into itself or  the wall.
"""

from turtle import Turtle
import turtle

# list for body sections , used with snake_body_creation method
body_sections = []


class Snake:
    """ Snake class has the basic functions to create and move a snake """

    def __init__(self, length=1, color="red", move="right", shape="square", size=0.5, position=(0, 0),
                 direction="right", speed=1):
        self.length = length
        self.color = color
        self.shape = shape
        self.move = move
        self.size = size
        self.position = position
        self.direction = direction
        self.speed = speed

    def snake_creation(self):
        """ Creates the snake head with default attributes """

        viper_head = Turtle(self.shape)
        viper_head.speed(self.speed)
        viper_head.shapesize(self.size, self.size)
        viper_head.penup()
        viper_head.goto(self.position)
        viper_head.color(self.color)

        return viper_head

    def snake_body_creation(self):
        """ Creates the segments of the snake body """

        viper_body = Turtle(self.shape)
        viper_body.speed(self.speed)
        viper_body.shapesize(0.5, 0.5)
        viper_body.penup()
        viper_body.goto(self.position)
        # add way to change colors with user input
        viper_body.color("orange")
        body_sections.append(viper_body)

        return body_sections

    # stores the direction from user input  and stops snake from going in reverse.
    def up(self):
        if self.direction != "down":
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.direction = "down"

    def right(self):
        if self.direction != "left":
            self.direction = "right"

    def left(self):
        if self.direction != "right":
            self.direction = "left"

    # calculates a new x and y cord variable and passes it back
    def prep_move_y(self, direction, cord_y):
        if direction == "up":
            cord_y = cord_y + 12
            return cord_y
        elif direction == "down":
            cord_y = cord_y - 12
            return cord_y
        else:
            return cord_y

    def prep_move_x(self, direction, cord_x):
        if direction == "right":
            cord_x = cord_x + 12
            return cord_x
        elif direction == "left":
            cord_x = cord_x - 12
            return cord_x
        else:
            return cord_x

    def move_body_sections(self, viper_body, viper_head):
        """ Reverses the order of segments and move the first section to the front"""
        for section in range(len(viper_body) - 1, 0, -1):
            viper_body[section].goto(viper_body[section - 1].xcor(), viper_body[section - 1].ycor())

        if len(viper_body) > 0:
            viper_body[0].goto(viper_head.xcor(), viper_head.ycor())


class SnakeCollision:
    """ Class that keeps methods for collision detection"""

    def __init__(self, ycor, xcor, body_length, viper_body, viper_head):
        self.ycor = ycor
        self.xcor = xcor
        self.body_length = body_length
        self.viper_body = viper_body
        self.viper_head = viper_head

    def wall_collision(self):
        """ checks if snake has run into the wall"""
        if self.xcor > 230 or self.xcor < -230 or self.ycor > 230 or self.ycor < -230:
            return True

    def self_collision(self):
        """ Checks if snake has run into itself. """
        for body_sec in self.viper_body:
            # prevents game from closing at start
            if self.xcor != 0 and self.body_length > 0:
                # compares distance of snake ahead and snake body
                if body_sec.distance(self.viper_head) < 10:
                    # update with different option of losing
                    return True
