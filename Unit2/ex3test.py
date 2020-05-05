'''
Test class for exercise 3 - base copied from exercise 1 test file
'''

import numpy as np
import matplotlib.pylab as pl
from exercise3 import MyGaussianPdf

def main():

    '''Sets values for easy changing in hard code'''
    mean = 0
    width = 1
    numpoints = 1000000
    values = []

    trail = MyGaussianPdf(mean, width, 0)   #initialises class, 0 for resetting the throw counter for numerical integration

    '''Loop to gather data using Gaussian class'''
    for i in range(numpoints):   #ensures right number of points recorded
        x1 = trail.evaluate()
        values.append(x1)

    analytic = trail.integralAnalytic()
    numeric = trail.integralNumeric(numpoints)   #numpoints is the number of 'hits' under curve for numerical integration

    print('Analytic result: ' + str(analytic))
    print('Numeric result: ' + str(numeric))

    pl.hist(values, bins = 100)   #plots histogram
    pl.show()

main()
