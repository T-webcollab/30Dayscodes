import turtle
from paddle import Paddle
from Ball import Ball
from scoreboard import  Score
import time
turtle.listen()
screen=turtle.Screen()
screen.tracer(0)

screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.title("PONG GAME")

ball=Ball()
right_score=Score((100,240))
left_score=Score((-100,240))



R_paddle=Paddle(350,0)
L_paddle=Paddle(-350,0)

screen.onkey(fun=R_paddle.move_up,key="Up")
screen.onkey(fun=R_paddle.move_down,key="Down")
screen.onkey(fun=L_paddle.move_up,key="w")
screen.onkey(fun=L_paddle.move_down,key="s")
is_game_over=True
while is_game_over:
    screen.update()
    time.sleep(ball.pace)
    ball.movement()

    #Detect collision with the ball
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()
    #Detect collision the paddle
    if ball.distance(R_paddle)<50 and ball.xcor()>330 or ball.distance(L_paddle)<50 and ball.xcor()<-330 :
        ball.x_bounce()
    if ball.xcor()>380:
        ball.refresh()
        left_score.update()

    if ball.xcor()<-380:
        ball.refresh()
        right_score.update()




screen.exitonclick()