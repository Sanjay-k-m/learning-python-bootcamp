from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()
def forward():
    turtle.forward(50)
def backward():
    turtle.backward(50)
def left():
    turtle.setheading(turtle.heading() +10 )
def right():
    turtle.setheading(turtle.heading() -10 )
def clear():
    turtle.penup()
    turtle.clear()
    turtle.home()
    turtle.pendown()

screen.onkey(forward, "Up")
screen.onkey(backward,"Down")
screen.onkey(left,"Left")

screen.onkey(clear,"c")

screen.listen()
screen.exitonclick()