'''
Checkpoint 2 chi squared minimisation
'''

'''
y = m*x + c
di**2 = ((ym - yp)/epsilon)**2
chisqr = sum of di**2 for i = 1 -> numpoints
'''

import math as m
import numpy as np

'''
Class for finding value of straight StraightLine
'''
def StraightLine(m, x, c):
    return (x * m) + c

'''
Class for finding Chi Squared, np.arrays passed for ym, x, eps
'''
def Chisq(ym, x, m, c, eps):
    chisq = 0
    yp = StraightLine(m, x, c)
    disq = ((ym - yp)/eps)**2.0
    for i in range(len(ym)):
        chisq += disq[i]

    return chisq

################################################################################
################################################################################
'''
Minimiser class
'''
class Minimisation(object):

    def __init__(self):
        self.iterations = 1
        self.m = 1
        self.dm = 1
        self.c = 1

    '''
    Sets the max number of iterations of Minimiser
    '''
    def setmaxit(self, numiterations):
        self.iterations = numiterations

    '''
    Sets initial paramters of the minimiser
    '''
    def setstartparam(self, mo, stepm, co):
        self.m = mo
        self.dm = stepm
        self.c = co

    '''
    Minimises the variable - is passed difference between 2 values of function
                             and either flips and halves step if first smaller or
                             continues at step if first smaller
    '''
    def minimise(self, funcval):
        if funcval < 0:   #1st < 2nd t.f. must reverse and shricnk step as minimum passed
            self.dm = (-1/2.0)*self.dm
            self.m += self.dm
        elif funcval > 0:   #1st > 2nd t.f. keep going as minimum not reached
            self.m += self.dm

    '''
    Runs the iterations
    '''
    def isfinished(self, ym, x, eps):
        cs1 = Chisq(ym, x, self.m, self.c, eps)
        self.m += self.dm
        cs2 = Chisq(ym, x, self.m, self.c, eps)

        for i in range(self.iterations):
            diff = cs1 - cs2
            self.minimise(diff)
            cs1 = cs2
            cs2 = Chisq(ym, x, self.m, self.c, eps)

        return self.m

################################################################################
################################################################################

def main():
    mguess = 0.5
    cguess = 1
    mstep = 0.005
    iterations = 1000

    filein = open("testdata.txt", "r")

    xdata = np.array([])
    ydata = np.array([])
    edata = np.array([])

    for line in filein.readlines():
        tokens = line.split("  ")
        xdata = np.append(xdata, float(tokens[0]))
        ydata = np.append(ydata, float(tokens[1]))
        edata = np.append(edata, float(tokens[2]))

    filein.close()

    min = Minimisation()
    min.setmaxit(iterations)
    min.setstartparam(mguess, mstep, cguess)
    minm = min.isfinished(ydata, xdata, edata)

    print(minm)

main()
