from turtle import *
shape('circle')
color(input('Anh thÝch mµu g× '))
pensize(15)
#4 h×nh thoi
#C¸i nµy lóc ®Çu em lµm nhÇm mét nöa xong nh×n l¹i hãa ra thµnh hay =)). P/s: §Þnh xãa mµ cho vµo lÊy 10+ :v
speed(5)
for i in range(8):
    right(30)
    forward(100)
    for i in range(3):
        if i %2==0:
            left(60)
        else:
            left(120)
        forward(100)
    for i in range(4):
        forward(100)
        if i%2==0:
            right(60)
        else:
            right(120)
clearscreen()
shape('turtle')
color('Red')
pensize(15)
right(30)
forward(100)
for i in range(3):
    if i %2==0:
        left(60)
    else:
        left(120)
    forward(100)
for i in range(4):
    forward(100)
    if i%2==0:
        right(60)
    else:
        right(120)
left(30)
forward(100)
for i in range(3):
    if i %2==0:
        left(60)
    else:
        left(120)
    forward(100)
for i in range(4):
    forward(100)
    if i%2==0:
        right(60)
    else:
        right(120)
# ®a gi¸c lång nhau víi mµu ch½n lÎ
clearscreen()
shape('circle')
pensize(10)
for i in range(3,7):
    if i%2!=0:
        color('Red')
    else:
        color('Blue')
    for j in range(i):
        forward(100)
        left(360/i)
#End.
clearscreen()
shape('circle')
pensize(15)
color('Purple')
penup()
backward(500)
pendown()
write('From Kh¸nh with luv <3',font=('.VnBahamasB',72,'normal'))

