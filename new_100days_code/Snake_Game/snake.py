from turtle import Turtle
import random
move_distance=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]


x = 0
y = 0

class Snake:

    def __init__(self):
        self.all_turtle=[]
        self.create_snake()
        self.head=self.all_turtle[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self,position):
        pen = Turtle("square")
        pen.color("white")
        pen.penup()
        pen.goto(position)
        self.all_turtle.append(pen)
    def extend(self):
        self.add_snake(self.all_turtle[-1].position())

    def move(self):
        for segment in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[segment - 1].xcor()
            new_y = self.all_turtle[segment - 1].ycor()
            self.all_turtle[segment].goto(new_x, new_y)
        self.all_turtle[0].forward(move_distance)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)










