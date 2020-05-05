'''
Exercise 2 - Rndm Num Gen
'''

'''
Uses numpy inbuilt gaussian function
'''

import numpy as np
import matplotlib.pyplot as pl

def main():

    '''Values for easy changing in hard code'''
    mean = 0
    width = 1
    numpoints = 1000

    data =  np.random.normal(mean, width, numpoints)

    pl.hist(data, bins = 50)
    pl.show()

main()
