from turtle import *
# 1.
speed(5)
bgcolor("black")
shape('circle')
pensize(10)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
c = 0
for i in range(3,8):
    color(colors[c])
    c +=1
    for j in range(i):
        forward(100)
        left(360/i)
# 2.
clearscreen()
speed(5)
bgcolor("black")
shape('circle')
pensize(10)
penup()
backward(200)
pendown()
c = 0
for i in range(5):
    begin_fill()
    color(colors[c])
    c +=1
    for i in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    forward(110)
    end_fill()
#End.
clearscreen()
pensize(15)
bgcolor("black")
color('Purple')
penup()
backward(500)
pendown()
write('From Kh¸nh with luv <3',font=('.VnBahamasB',72,'normal'))
    
