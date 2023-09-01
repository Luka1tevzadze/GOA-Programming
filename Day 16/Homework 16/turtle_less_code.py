from turtle import *

width(5)
speed(15)

def walls():
    for i in range(4):
        forward(200)
        left(90)
walls()

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

def roof1():
    color("red")
    begin_fill()
    right(150)
    forward(200)
    left(120)
    forward(200)
    end_fill()
roof1()

penup()
goto(60, 160)
pendown()

def windows():
    color("cyan")
    begin_fill()
    right(60)
    forward(32)
    left(90)
    forward(30)
    left(90)
    forward(30)
    left(90)
    forward(32)
    end_fill()
windows()

penup()
goto(160, 125)
pendown()
def second_window():
    color("cyan")
    begin_fill()
    right(60)
    forward(32)
    left(90)
    forward(30)
    left(90)
    forward(30)
    left(90)
    forward(32)
    end_fill()

exitonclick()