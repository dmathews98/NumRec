'''
Exercise 1 - Rndm Num Gen: Arbitrary Dist
'''

'''
Class for developing a Gaussian distribution and
plotting a histogram of the results

f(x) = exp(-(x-mew)^2 / 2 sigma^2)    -    Gaussian

mew = mean, sigma = width

Take [a, b] -> [-4, 4] ... max = 1 so take f as 1.01
'''

import numpy as np
import math as m

class MyGaussianPdf(object):

    '''Constructor'''
    def __init__(self, dblmean, dblwidth):
        self.mew = dblmean   #saves mean
        self.sigma = dblwidth   #saves width
        self.fmax = 1.01   #saves fmax

    '''Produces random x value and converts to range being used'''
    def next(self):
        x1 = np.random.uniform()   #random number
        x1 = -4 + (4-(-4))*x1    #converts random number to range

        return x1

    ''' Evaluates y at the random x, and produces another y to compare, returns x if suitable'''
    def evaluate(self, x):
        y1 = m.exp(-(x-(self.mew))**2 / (2 * (self.sigma)**2))   #f(x1) for suitability
        y2 = np.random.uniform()   #random y value
        y2 = self.fmax*y2   #converted to range

        if y2 < y1:   #if within curve, then x returned, else it is discarded
            return x
        else:
            return False
