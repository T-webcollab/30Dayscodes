import turtle
from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake Game")
turtle.listen()



snake=Snake()
'''Create a snake object'''
food=Food()
"""Create a food object"""
score=Score()
"""Create the score board that shows score every time it the snake eats the touches the food.
    """
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.right,key="Right")
screen.onkey(fun=snake.left,key="Left")

is_game_over=True
while is_game_over:
    screen.update()
    """ Update the screen every 0.1 seconds ."""
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()# Update the position of food every time the snake touches the food
        snake.extend()# Everytime the snake touches the food the length of snakes increases .
        score.add_score() # Add the score when the snake touches the object.

    if snake.head.xcor()>300 or snake.head.ycor()>300 or snake.head.xcor()<-300 or snake.head.ycor()<-300:
        score.when_over()
        is_game_over=False# When the snake head touches the end of the screen the game is over.
    for body in snake.all_turtle[1:]:
        if snake.head.distance(body)<10:# When the snake head touches or comes near its own body the game is over
            score.when_over()
            is_game_over=False







screen.exitonclick()

