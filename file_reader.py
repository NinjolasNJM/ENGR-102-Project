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
        distance and the distance's unit. At first it was unclear whether there would be two kinds of steps
        for moving and turning, but eventually it was clear that each step separated by a blank line had both
        a turning part and a moving part. The moving part was assigned to a
        unit of measurement, and at first just these three variables
        were stored in a step. However, some words for directions such as 'slight'
        implied a different angle than other turns, so in the end the kind of direction instruction
        is also returned. Each variable also required a default value, since otherwise a
        value of None would produce an error.'''
        dir = 'onto'
        move = 0
        unit = 'Nothings'
        dirkind = 'continue'
        dirKinds = ['turn', 'head', 'continue', 'slight', 'keep']
        moveKinds = ['mi', 'ft']
        for i in range(len(step)):
            if str.lower(step[i]) in dirKinds:
                dir = step[i + 1]
                dirkind = step[i]
            if str.lower(step[i]) in moveKinds:
                move = step[i - 1]
                unit = step[i]

        return dir, move, unit, dirkind

    def makeInstructions(self):
        ''' NinjolasNJM2003@gmail.com

        Makes a list with each instruction in it. For the sake of simplicity, it
        also removes any instruction that has no direction in it. This makes the console output simpler.'''
        instr = [self.makeStep(f) for f in self.file]
        for i in instr:
            if i[1] == 0:
                instr.remove(i)
        return instr

    def stepToString(self, step):
        ''' NinjolasNJM2003@gmail.com

        Returns a String describing the step that is taken. Had to take into account the kind
        of direction and every part of the step object.'''
        (dir, move, unit, dirkind) = step
        return( dirkind.capitalize() + ' ' + dir + ' ' + str(move) + ' ' + unit)

    def __str__(self):
        ''' NinjolasNJM2003@gmail.com

        Returns a String of all the steps.'''
        return '\n'.join([self.stepToString(s) for s in self.makeInstructions()])
