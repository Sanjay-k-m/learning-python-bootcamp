# from turtle import Turtle,Screen
# # from turtle import Turtle as t
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("green")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from turtle import Turtle,Screen
s = Screen()

t = Turtle()

for _ in range(20):

    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
s.exitonclick()