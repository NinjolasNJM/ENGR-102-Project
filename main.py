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

# run code:
# get steps as a list of each word in each step that is separated by a blank line.
file1 = 'Kyle2VetPk.txt'
file2 = 'Easterwood2Coulter.txt'
file3 = 'Zach2StJo.txt'

gui=GUI()
file_name=gui.file
file_name=file_name.split('\n')[0]
s = gui.speed


def codeToRun(fileName,s):
    steps = Instructions(fileName)
    print(steps)
    drive = Drive(fileName, 500,600,s)
    drive.run(steps.makeInstructions())


codeToRun(file_name,s)









