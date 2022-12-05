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
class Instructions:
    '''NinjolasNJM2003@tamu.edu

    '''
    def __init__(self, name):
        '''NinjolasNJM2003@tamu.edu

        Opens a file and converts the instructions so that it is a list
        with the space-separated words of each step which was separated
        by a single blank line.
        '''
        self.file = [s.replace('\n', ' ').replace('(', '').replace(')', '').split() for s in open(name).read().split('\n\n')]

    def makeStep(self, step):
        ''' NinjolasNJM2003@gmail.com

        Takes a list of strings and gets the parts of the step from it.
        Looks for keysords like "turn" and "ft" for determining where the direction and
        move distance, respectively, are defined, and returns the direction,
        distance and the distance's unit.'''
        dir = None
        move = None
        unit = None
        dirKinds = ['turn', 'head', 'continue', 'slight']
        moveKinds = ['mi', 'ft']
        for i in range(len(step)):
            if str.lower(step[i]) in dirKinds:
                dir = step[i + 1]
            if str.lower(step[i]) in moveKinds:
                move = step[i - 1]
                unit = step[i]

        return dir, move, unit

    def makeInstructions(self):
        ''' NinjolasNJM2003@gmail.com

        Makes a list with each instruction in it'''
        instr = [self.makeStep(f) for f in self.file]
        return instr
