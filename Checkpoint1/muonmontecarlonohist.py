'''
Checkpoint 1 - Muon Lifetime
'''

'''
Class that determines the lifetime of a muon, using probability of decay

Also finds average lifetime from passed array

P(t) = (1/tau)exp(-ti/tau)
'''

import numpy as np
import math as m

class MuonDecay(object):

    '''Constructor'''
    def __init__(self, tau):
        self.lmda = 1.0 / tau   #lambda ie 1/tau
        self.fmax = (1.0 / tau) + 0.0001  #saves fmax; slightly above for monte carlo method

    '''Produces random x value and converts to range being used'''
    def next(self):
        t1 = np.random.uniform()   #random number [0, 1]
        t1 = 1e-4*t1   #converts random number to range(high range so as effectively infinity)

        return t1

    ''' Evaluates y at the random x, and produces another y to compare, returns x if suitable'''
    def evaluate(self):
        j = 0   #initialiser for loop
        while j == 0:   #loop that breaks only when viable point found
            t1 = self.next()   #calls random range adjusted time
            y1 = self.lmda * m.exp((-self.lmda) * t1)   #f(t1) for suitability
            y2 = np.random.uniform()   #random y value
            y2 = self.fmax*y2   #converted to range

            if y2 < y1:   #if within curve, then x returned, else it is discarded
                return t1

    '''Finds average lifetime of the data set passed'''
    def averagelifetime(self, values, numpoints):
        total = 0   #ensures resets each time called

        for j in range(numpoints):   #finds cumulative total of average lifetimes
            total += values[j]

        average = total / numpoints

        return average

    '''Repeats evaluation to complete one experiment for given number of repetitions'''
    def repetitions(self, points):
        times = []   #initialises time array
        for i in range(points):   #loop for number of points in one experiment
            t1 = self.evaluate()
            times.append(t1)

        av = self.averagelifetime(times, points)   #finding average lifetime

        return av
