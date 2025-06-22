from turtle import Turtle
ALIGNMENT='center'
FONT=("courier",16,'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.add_score()

    def add_score(self):
        self.clear()
        self.goto(0, 275)
        self.color("white")
        self.write(f'Score :{self.score}', True, ALIGNMENT, FONT)
        self.score+=1
    def  when_over(self):
        self.home()
        self.color("white")
        self.write("GAME OVER",True,ALIGNMENT,FONT)



