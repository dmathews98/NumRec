'''
Exercise 1 test file
'''

import numpy as np
import matplotlib.pylab as pl
from exercise1 import MyGaussianPdf

def main():

    '''Sets values for easy changing in hard code'''
    dblmean = 0
    dblwidth = 1
    numpoints = 1000
    values = []

    trail = MyGaussianPdf(dblmean, dblwidth)   #initialises class

    for i in range(numpoints):   #ensures right number of points recorded
        j = 0
        while j == 0:   #continus loop until valid x value found
            x1 = trail.next()
            y2 = trail.evaluate(x1)
            if y2 != False:   #correct value found so it is appended to data and loop broken to add to number of values counter
                values.append(x1)
                j += 1   #breaks loop

    pl.hist(values, bins = 50)   #plots histogram
    pl.show()

main()
