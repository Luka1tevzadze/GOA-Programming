from turtle import *

# making my first house in python

# the walls

width(5)
speed(15)

forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)


# finished walls

# drawing door


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

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# end of making door & roof

# making windows


penup()
goto(60, 160)
pendown()

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

# Second Window

penup()
goto(160, 125)
pendown()

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


print("Luka Tevzadze" + " 10 Years Old!" + " Got intersted in programming when i was 8. pretty young age yea?")

exitonclick()