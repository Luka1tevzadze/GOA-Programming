from turtle import *

width(7)
speed(100)

def triangle():
    for i in range(3):
        right(60)
        forward(200)
        right(60)
triangle()

ask_user = input("what is the perimeter of the triangle? : ")

print("the perimeter of the triangle is " + ask_user)

exitonclick()