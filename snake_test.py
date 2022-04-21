"""
Temp file for me to test snake class methods
"""

from snake import Snake
from snake import SnakeCollision
from turtle import Screen, Turtle
import time
from food import Food
from score import Score


def button():
    snake_game()

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
    main_screen.onKey(button(), "r")



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
            Score.text_at_xy(self,0,0,"You lost!")
            Score.text_at_xy(self,0,-50,"Click to play it again")
            Turtle.onclick(button(), 1)


        # checks for collision into self
        if collision.self_collision() == True:
            main_screen.clear()
            viper_attributes.clear_body()
            food.hide_food()

            Score.text_at_xy(self,0,0,"You lost!")
            Score.text_at_xy(self,0,-50,"Click to play it again")




        # moves the snake body sections around
        viper_attributes.move_body_sections(viper_body, viper_head)

        # Michelles Code, ended up not needind it:
        # Moving the food to a random location
        # print(food.track_location())
        # print(viper_head.distance(food.track_location()))

        if viper_head.distance(food.track_location()) < 20:
            Food.random_location(food, 0, 240, 0, 240)
            # creates the snake body object
            viper_body = viper_attributes.snake_body_creation()
            # moves new body correct location
            viper_attributes.move_body_sections(viper_body, viper_head)
            # score updating
            score = Score.increment_score(self, score, 10)
            Score.show_score(self, score)

        if score == 20:
            main_screen.clear()
            viper_attributes.clear_body()
            Score.text_at_xy(self, 0, 0, "You won!")
            Score.text_at_xy(self, 0, -50, "Click to play it again")


        # delayed used to slow down game
        delay = 0.1
        time.sleep(delay)



snake_game()
