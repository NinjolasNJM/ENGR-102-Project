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

class Drive:
    '''vegbtefb'''
    def __init__(self, windowHeight=500, windowWidth=600, speed=2, shape=("circle"), bColor="white"):
        self.speed = speed
        self.shape = shape
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.bColor = bColor

    def turn(self, d):
        direction = d.lower()
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

    def move(self, move, unit):
        dist = float(move) * 20 / 5280 if unit == 'ft' else float(move) * 20
        forward(dist)

    def takeStep(self, step):
        (dir, move, unit) = step

        self.turn(dir)
        self.move(move, unit)

    def run(self, steps):
        screensize(self.windowWidth, self.windowHeight, self.bColor)


        speed(self.speed)
        for s in steps:
            self.takeStep(s)

        exitonclick()

