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

import turtle

class Instr:
    '''NinjolasNJM2003@tamu.edu'''
    def __init__(self, kind, value):
        self.direction = 0
        self.distance = 2

        if kind == 'turn':
            self.direction = value
        elif kind == 'move':
            self.distance = value

    #def execute(self):
        #output.turn(direction)
        #output.move(distance)

# run code:
# get steps as a list of each word in each step that is separated by a blank line.
file1 = 'Kyle2VetPk.txt'
file2 = 'Easterwood2Coulter.txt'
file3 = 'Zach2StJo.txt'

steps = [s.replace('\n', ' ').replace('(', '').replace(')', '').split() for s in open(file3).read().split('\n\n')]

def makeStep(step):
    '''Takes a list of strings and gets the parts of the step from it.
    Looks for keysords like "turn" and "ft" for determining where the direction and
    move distance, respectively, are defined, and returns the direction,
    distance and the distance's unit.'''
    dir = None
    move = None
    unit = None
    dirKinds = ['turn', 'head', 'continue']
    moveKinds = ['mi', 'ft']
    for i in range(len(step)):
        if str.lower(step[i]) in dirKinds and dir is None:
            dir = step[i + 1]
        if str.lower(step[i]) in moveKinds and move is None:
            move = step[i - 1]
            unit = step[i]

    return dir, move, unit

for s in steps:
    print(makeStep(s))








