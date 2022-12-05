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
from turtle_graphic import Car


# run code:
# get steps as a list of each word in each step that is separated by a blank line.
file1 = 'Kyle2VetPk.txt'
file2 = 'Easterwood2Coulter.txt'
file3 = 'Zach2StJo.txt'

steps1 = Instructions(file1)
steps2 = Instructions(file2)
steps3 = Instructions(file3)

print(steps2.makeInstructions())
car = Car(1)
car.run(steps2.makeInstructions())









