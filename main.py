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

from file_reader import Instructions
from turtle_graphic import Drive
from gui import GUI

def getVars():
    ''' @elivalentino@tamu.edu

    Creates the GUI and uses it to create the instructions
    and speed variables.

    '''
    gui=GUI()
    file_name=gui.file
    file_name=file_name.split('\n')[0]
    s = gui.speed
    return file_name, s


def codeToRun(fileName,s):
    '''@NinjolasNJM2003@tamu.edu

    The code that runs the GUI, getting the input and
    the turtle output. Additionally prints the steps to the console.
    '''
    steps = Instructions(fileName)
    print(steps)
    drive = Drive(fileName, 500,600,s)
    drive.run(steps.makeInstructions())

file_name, s = getVars()
codeToRun(file_name,s)









