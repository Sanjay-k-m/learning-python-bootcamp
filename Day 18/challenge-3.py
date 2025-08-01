from turtle import Turtle,Screen

t= Turtle()
s = Screen()
circle = 440
sides =3


def draw_shape(num_sides):


    angle = circle / num_sides
    for _ in range(num_sides):
         t.forward(100)
         t.right(angle)



while sides < 1000:
    draw_shape(sides)
    sides += 1

s.exitonclick()









s.exitonclick()