from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.pensize(2)
        self.y=10
        self.x=10
        self.pace=0.1
        self.refresh()

    def movement(self):
        xcor=self.xcor()+self.x
        ycor=self.ycor()+self.y
        self.goto(xcor,ycor)
    def y_bounce(self):
        self.y=self.y *(-1)
    def x_bounce(self):
        self.x=self.x*(-1)
        self.pace*=0.9
    def refresh(self):
        self.goto(0,0)
        self.pace=0.1
        self.x_bounce()



