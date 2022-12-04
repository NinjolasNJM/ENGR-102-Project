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





speed(1)
setheading(90)

forward(50)
turn('southeast')
forward(100)
turn('southwest')
forward(100)
turn('onto')
forward(200)
turn('left')
forward(100)
turn('right')
forward(50)
turn('north')
forward(300)
turn('straight')
forward(500)

heading()

exitonclick()



#Make function for turning

#Make function for