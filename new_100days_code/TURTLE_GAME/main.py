import turtle
import random
is_race_on=False

screen =turtle.Screen()
screen.setup(500,400,0,0)
user=screen.textinput("User_choice","Which colour you want to bet")
colour= ['red', 'violet', 'blue', 'green', 'orange', 'black', 'indigo','brown']

pen = turtle.Turtle()
pen.color(user)
colour.remove(user)
pen.shape("turtle")
pen.up()
x=-230
y=-100
pen.goto(x,y)
all_turtle=[]
all_turtle.append(pen)
for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    y+=30
    new_turtle.goto(x, y)
    color=random.choice(colour)
    new_turtle.color(color)
    all_turtle.append(new_turtle)

    colour.remove(color)
if user:
    is_race_on=True
distance=[4,5,6,8,10]
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            if turtle.pencolor()==user:
                print(f"you win {turtle.pencolor()} has won")
            elif turtle.xcor()>230:
                print(f"You lose {turtle.pencolor()} has won the race")
        random_dist=random.choice(distance)
        turtle.forward(random_dist)

screen.listen()



screen.exitonclick()
