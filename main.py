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

class Instr:
    def __init__(self, kind, value):
        self.direction = 0
        self.distance = 0

        if kind == 'turn':
            self.direction = value
        elif kind == 'move':
            self.distance = value

# If instruction is a direction:
    # direction = direction types[next element of the list]
# else:
    # distance = prevfious element of the list * size of unit[kind]


# somethnig like that


