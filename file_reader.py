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
        dir = 'Continue'
        move = 0
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


# EV

class instructions2:

    def __init__(self,filename):
        file = open(filename)
        self.list1 = list(file)

    def getsimple(self,s, num, unit):
        liststring = s.split()
        direction = 'Continue'
        changedirection = ['turn', 'slight', 'head']
        for t in range(len(liststring)):
            if liststring[t].lower() in changedirection:
                direction = liststring[t + 1]
        return direction + ' ' + num + ' ' + unit + '\n'

    def getreal(self):
        simpledirections = ''

        changedirection = ['turn', 'slight', 'head']
        units = ['mi', 's', 'ft', 'min']
        time = ['s', 'min']

        for i in range(len(list1)):
            test = list1[i].split()

            if len(test) > 1:
                maybenum = test[0]
                maybenum = maybenum.replace('.', '')
                s = ''
                x = i - 1
                if maybenum.isnumeric() and test[1] in units:
                    while list1[x] != '\n' and x != -1:
                        s = list1[x] + s
                        x -= 1

                    dist = test[0]
                    unit = test[1]
                    if unit in time:
                        dist = test[2].replace('(', '')
                        unit = test[3].replace(')', '')

                    simpledirections += getsimple(s, dist, unit)
        return simpledirections
