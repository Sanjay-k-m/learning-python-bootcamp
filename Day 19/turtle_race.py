import random
from turtle import  Turtle,Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color : ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]

turtles = []

for turtle_index in range(0,len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_positions[turtle_index])
    turtles.append(new_turtle)

game_end = False

while not game_end:

    for turtle in turtles:
        if turtle.xcor() >240:
            game_end = True
            if turtle.pencolor == user_bet:
                print(f"You Win ! winner is  {turtle.pencolor()} turtle")
            else:
                print(f"You Lose ! winner is  {turtle.pencolor()} turtle")
            break

        turtle.forward(random.randint(0,10))
screen.exitonclick()