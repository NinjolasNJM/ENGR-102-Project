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

    Class that handles the file input and converts it into steps that can be used
    by the Drive class to draw the car's route.
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
        Looks for keywords like "turn" and "ft" for determining where the direction and
        move distance, respectively, are defined, and returns the direction,
        distance and the distance's unit.'''
        dir = 'onto'
        move = 0
        unit = 'Nothings'
        dirKinds = ['turn', 'head', 'continue', 'slight', 'keep']
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
        for i in instr:
            if i[1] == 0:
                instr.remove(i)
        return instr

    def stepToString(self, step):
        ''' NinjolasNJM2003@gmail.com

        Returns a String describing the step that is taken.'''
        (dir, move, unit) = step
        return('Go ' + dir + ' ' + str(move) + ' ' + unit)

    def __str__(self):
        ''' NinjolasNJM2003@gmail.com

        Returns a String of all the steps.'''
        return '\n'.join([self.stepToString(s) for s in self.makeInstructions()])
