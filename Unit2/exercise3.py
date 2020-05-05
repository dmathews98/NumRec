'''
Exercise 3 - Numerical Integration; copy and pasted base exercise 1 as req.
'''

'''
f(x) = exp(-(x-mew)^2 / 2 sigma^2)    -    Gaussian

mew = mean, sigma = width

Take [a, b] -> [-5sigma, 5sigma] ... max = sigma(2*pi)^(1/2) so add small amount to ensure just above

Area of box = 10*sigma * (sigma(2*pi)^(1/2))
F = successful hits / total hits
Total area under curve = Area of box * F
'''

import numpy as np
import math as m

class MyGaussianPdf(object):

    '''Constructor'''
    def __init__(self, mean, width, initialiser):
        self.mew = mean   #saves mean
        self.sigma = width   #saves width
        self.fmax = 1 + 0.00001   #saves fmax
        self.throws = initialiser   #counter for number of attempts at x1 values for numerical integration

    '''Produces random x value and converts to range being used'''
    def next(self):
        x1 = np.random.uniform()   #random number
        x1 = -(self.sigma)*5 + ((self.sigma)*5-(-(self.sigma)*5))*x1    #converts random number to range

        return x1

    ''' Evaluates y at the random x, and produces another y to compare, returns x if suitable'''
    def evaluate(self):
        j = 0   #initialiser for loop
        while j == 0:   #loop that breaks only when viable point found
            x1 = self.next()
            y1 = m.exp(-(x1-(self.mew))**2 / (2 * (self.sigma)**2))   #f(x1) for suitability
            y2 = np.random.uniform()   #random y value
            y2 = self.fmax*y2   #converted to range

            self.throws += 1   #counter increase for numerical integration

            if y2 < y1:   #if within curve, then x returned, else it is discarded
                return x1

    '''Computes analytical result for area under curve'''
    def integralAnalytic(self):
        result = self.sigma * (2*m.pi)**(1.0/2.0) #standard for gaussian

        return result

    '''Uses Monte Carlo Box method with a rectangle to compute area under curve'''
    def integralNumeric(self, hits):
        boxarea = 10*self.sigma * self.fmax   #area of box, x axis length * height
        hitratio = hits*1.0/(self.throws)   #the hit ratio
        curvearea = boxarea * hitratio   #area under curve

        return curvearea
