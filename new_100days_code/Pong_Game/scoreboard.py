from turtle import Turtle
align="center"
FONT=("courier",24,'normal')
class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.position=position

        self.hideturtle()
        self.color("white")
        self.score=0
        self.update()
    def update(self):

        self.clear()
        self.goto(self.position)
        self.write(f"Score:{self.score}",True,align,FONT)
        self.score+=1

