from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(4,1)
        self.color("white")
        self.x=xcor
        self.y=ycor
        self.goto(self.x,self.y)
    def move_up(self):
        ycor=self.ycor()+20
        self.goto(self.xcor(),ycor)
    def move_down(self):
        ycor=self.ycor()-20
        self.goto(self.xcor(),ycor)
