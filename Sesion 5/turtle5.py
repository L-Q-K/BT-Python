from turtle import *
import time

#Ex 1+2: Co trong sach thinkcspy3 =))

shape('turtle')
speed(0)

def draw_square ( side , _color):
    bgcolor('black')
    color(_color)
    for i in range(4):
        forward(side)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

time.sleep(5)
clearscreen()

#Ex 2+3:

shape('turtle')

def draw_star(x, y, side):
    bgcolor('black')
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(side)
        right(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

time.sleep(5)
clearscreen()
