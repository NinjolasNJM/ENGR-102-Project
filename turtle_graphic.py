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
    def __init__(self, windowHeight=500, windowWidth=600, speed=2, shape=("circle"), bColor="white", bgFile=('colors.png')):
        self.speed = speed
        self.shape = shape
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.bColor = bColor

    """
    chris.26@tamu.edu
    
    Defines a function called 'turn' that takes a string as a parameter, the string being a direction. 
    Function uses an 'if-else' command to turn the turtle icon to the desired direction stated by the parameter.
    """
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

    """
    chris.26@tamu.edu
    
    Defines a function called 'move' that takes 'move' and 'unit' as parameters, which are then put into a formula 
    to calculate the distance required to move.
    """
    def move(self, move, unit):
        dist = float(move) * 20 / 5280 if unit == 'ft' else float(move) * 20
        forward(dist)

    """
    chris.26@tamu.edu
    
    Defines a function called 'takeStep' that takes 'step' as a parameter which is used to hold three parameters: 
    direction, move, and unit. These control the movements of the turtle graphic via run function explained below.
    """
    def takeStep(self, step):
        (dir, move, unit) = step

        self.turn(dir)
        self.move(move, unit)

    """
    chris.26@tamu.edu
    
    Defines a function called 'run' in the 'Drive' class that takes parameter 'steps'. Uses a 'for-loop' to loop through
    'steps' to run into the turtle graphic. Uses command 'exitonclick' so that the turtle graphic does not disappear 
    after completely executing, and will disappear once the user clicks the screen. Also uses parameters stated earlier 
    in the class to set the screensize of the turtle window.
    """
    def run(self, steps):
        screensize(self.windowHeight, self.windowWidth, self.bColor)

        bgpic('colors.png')  # image should be PNG or GIF
        update()  # to show the image
        speed(self.speed)
        for s in steps:
            self.takeStep(s)

        exitonclick()

    """
    chris.26@tamu.edu
    
    Sets a background to the turtle graphic 
    window using a PNG file or GIF file
    """
    def winBackground(self):
        window = Screen()
        window.bgpic(f'{bgFile}')  # image should be PNG or GIF
        window.update()  # to show the image