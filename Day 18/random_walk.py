from turtle import Turtle,Screen
import random
from  colors import colors


tim = Turtle()

#random pick

def random_walk():
    angle_range = [0,90,180,270]
    tim.color(random.choice(colors))
    tim.speed(1000)
    tim.pensize(10)
    tim.shape(random.choice(['arrow', 'classic', 'turtle', 'circle', 'square', 'triangle']))
    random_num = random.randint(0,len(angle_range)-1)
    tim.setheading(angle_range[random_num])
    tim.forward(50)
loop = 0
while loop < 1000000:
    random_walk()
    loop +=1




