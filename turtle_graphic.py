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
    def __init__(self, title, windowHeight=500, windowWidth=600, speed=2, shape=("circle"), bColor="white", bgFile=('colors.png')):
        """
        chris.26@tamu.edu

        Sets parameters listed above with 'self' for the class 'Drive',, Holds parameters for other functions
        within this class, and sets parameters with values, such as the window width and height of the turtle
        graphic screen.
        """
        self.title = title
        self.speed = speed
        self.shape = shape
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.bColor = bColor


    def turn(self, d):
        """
            chris.26@tamu.edu

            Defines a function called 'turn' that takes a string as a parameter, the string being a direction.
            Function uses an 'if-else' command to turn the turtle icon to the desired direction stated by the parameter.
            """
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
        """
            chris.26@tamu.edu

            Defines a function called 'move' that takes 'move' and 'unit' as parameters, which are then put into a formula
            to calculate the distance required to move.
            """
        dist = float(move) * 30 / 5280 if unit == 'ft' else float(move) * 30
        forward(dist)


    def takeStep(self, step):
        """
            chris.26@tamu.edu

            Defines a function called 'takeStep' that takes 'step' as a parameter which is used to hold three parameters:
            direction, move, and unit. These control the movements of the turtle graphic via run function explained below.
            """
        (dir, move, unit) = step

        self.turn(dir)
        self.move(move, unit)


    def run(self, steps):
        """
            chris.26@tamu.edu

            Defines a function called 'run' in the 'Drive' class that takes parameter 'steps'. Uses a 'for-loop' to loop through
            'steps' to run into the turtle graphic. Uses command 'exitonclick' so that the turtle graphic does not disappear
            after completely executing, and will disappear once the user clicks the screen. Also uses parameters stated earlier
            in the class to set the screensize of the turtle window.
            Sets background of turtle graphic window to file stated.
            """
        screensize(self.windowHeight, self.windowWidth, self.bColor)

        title(self.title)
        bgpic('colors.png')  # image should be PNG or GIF
        update()  # to show the image
        speed(self.speed)
        color('#555555', '#a71810')
        for s in steps:
            self.takeStep(s)

        exitonclick()
