"""
Temp file for me to test snake class methods

"""

from snake import Snake
from snake import SnakeCollision
from turtle import Screen, Turtle
import time

from food import Food
import random

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

# Michelles code
# Setting up the food object.
food = Food(Turtle(), 0, 100, "red", "circle")

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
    collision.wall_collision()
    # checks for collision into self
    collision.self_collision()

    # moves the snake body sections around
    viper_attributes.move_body_sections(viper_body, viper_head)

    # Michelles Code
    # Moving the food to a random location

    if viper_head.distance(food.track_location()) < 20:
        print("IT worked")
        Food.random_location(food, 0, 240, 0, 240)
        # creates the snake body object
        viper_body = viper_attributes.snake_body_creation()

    # if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:

    # print(food.xpos)
    # SnakeCollision.food_collision(food.xpos)


    # delayed used to slow down game
    delay = 0.1
    time.sleep(delay)
