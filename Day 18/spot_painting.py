import  random
from turtle import  Screen,Turtle
from typing import runtime_checkable

from colorgram_program import  get_colors
turtle = Turtle()

screen = Screen()
screen.colormode(255)
turtle.penup()
turtle.setx(-400)
turtle.sety(-400)
turtle.pendown()
turtle.pensize(10)
color_array = get_colors()
loop = 0
while loop !=10:
    for i in range(10):
        turtle.pencolor(random.choice(color_array))
        turtle.down()
        turtle.dot()
        turtle.penup()
        turtle.forward(60)
    # turtle.penup()
    turtle.right(270)
    turtle.forward(60)
    turtle.left(90)

    for i in range(10):
        turtle.pencolor(random.choice(color_array))
        turtle.penup()


        turtle.forward(60)

    turtle.left(180)
    loop+=1
screen.exitonclick()