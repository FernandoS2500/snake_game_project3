"""
Temp file for me to test snake class methods

"""

from snake import Snake
from snake import SnakeCollision
from turtle import Screen
import time

# setup main window
main_screen = Screen()
main_screen.setup(width=500, height=500)
main_screen.bgcolor("white")
main_screen.title("Team 3 Snake Game")
main_screen.tracer(0)

# creates the snake object
viper_attributes = Snake()
viper_head = viper_attributes.snake_creation()

# creates the snake body object
viper_body = viper_attributes.snake_body_creation()

# binds keys
main_screen.listen()
main_screen.onkey(viper_attributes.up, "Up")
main_screen.onkey(viper_attributes.down, "Down")
main_screen.onkey(viper_attributes.right, "Right")
main_screen.onkey(viper_attributes.left, "Left")

# used for viper body sections
key = 5

# main game loop
while True:

    # sets the new x and y cor
    viper_head.setx(viper_attributes.prep_move_x(viper_attributes.direction, viper_head.xcor()))
    viper_head.sety(viper_attributes.prep_move_y(viper_attributes.direction, viper_head.ycor()))

    # screen update
    main_screen.update()

    # Checks for collision into wall
    collision = SnakeCollision(viper_head.xcor(), viper_head.ycor(), len(viper_body), viper_body, viper_head)
    collision.wall_collision()
    # checks for collision into self
    collision.self_collision()

    # moves the snake body sections around
    viper_attributes.move_body_sections(viper_body, viper_head)

    # temp way to add extra sections to snake
    while key < 30:
        # creates the snake body object
        viper_body = viper_attributes.snake_body_creation()
        key = key + 1

    # delayed used to slow down game
    delay = 0.1
    time.sleep(delay)
