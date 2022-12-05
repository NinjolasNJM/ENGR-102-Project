# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Nicholas Mirabal
#               Eli Valentino
#               Chris Avila
# Section:      102-565
# Assignment:   Project
# Date:         6 December 2022

from turtle import *

def turn(direction):
    if direction == 'north':
        setheading(90)#Sets direction to north when using a objective direction
        left(0)
    elif direction == 'east':
        setheading(90)
        right(90)
    elif direction == 'south':
        setheading(90)
        right(180)
    elif direction == 'west':
        setheading(90)
        left(90)
    elif direction == 'northeast':
        setheading(90)
        right(45)
    elif direction == 'southeast':
        setheading(90)
        right(135)
    elif direction == 'northwest':
        setheading(90)
        left(45)
    elif direction == 'southwest':
        setheading(90)
        left(135)
    elif direction == 'left':

        left(90)
    elif direction == 'right':

        right(90)
    elif direction == 'onto':

        left(0)
    else:
        left(0)

"""
setup(500, 550)
title('Kyle Field to Veterans Park')
speed(1)
setheading(90)



turn('southeast')
forward(20)
turn('left')
forward(110)
turn('left')
forward(30)
turn('right')
forward(140)
turn('left')
forward(20)
turn('right')
forward(80)
turn('right')
forward(40)

exitonclick()

"""

#Make function for turning

#Turtle Shape
speed(1)
penup()
left(180)
forward(200)
left(180)
pendown()
forward(50)
right(90)
circle(50, 180)
right(90)
forward(100)
right(90)
circle(50, 180)



exitonclick()


class Car:

    def __init__(self, windowHeight=500, windowWidth=600, speed=2):
        speed(speed)

    def turn(direction):
        if direction == 'north':
            setheading(90)  # Sets direction to north when using a objective direction
            left(0)
        elif direction == 'east':
            setheading(90)
            right(90)
        elif direction == 'south':
            setheading(90)
            right(180)
        elif direction == 'west':
            setheading(90)
            left(90)
        elif direction == 'northeast':
            setheading(90)
            right(45)
        elif direction == 'southeast':
            setheading(90)
            right(135)
        elif direction == 'northwest':
            setheading(90)
            left(45)
        elif direction == 'southwest':
            setheading(90)
            left(135)
        elif direction == 'left':

            left(90)
        elif direction == 'right':

            right(90)
        elif direction == 'onto':

            left(0)
        else:
            left(0)
