from turtle import *

width(7)
speed(100)

def cube():
    for i in range(4):
        forward(200)
        left(90)
cube()

ask_user_for_area = input("What is the area of the cube? : ")
ask_user_for_perimeter = input("What is the perimeter of the cube? : ")

print("The area of the cube is " + ask_user_for_area)
print("The Perimeter of the cube is " + ask_user_for_perimeter)

exitonclick()