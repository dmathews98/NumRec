'''
Test file for Checkpoint 1 - Muon Decay by MonteCarlo
'''

import numpy as np
import matplotlib.pylab as pl
from muonmontecarlo import MuonDecay

def main():

    '''Sets values for easy changing in hard code'''
    tau = 2.2e-6   #characteristic lifetime
    numpoints = 1000   #number of decay times to be recorded
    avtimes = []   #average lifetime per run stored here
    runs = 500   #number of experiment repetions

    '''Loop for each run of experiment'''
    for k in range(runs):
        trail = MuonDecay(tau)   #initialises class, repeated for each experiment to reset
        timeinrun = []   #here to ensure resets each experiment run
        '''Loop to gather data using Decay class'''
        for i in range(numpoints):   #ensures right number of points recorded
            t1 = trail.evaluate()   #finds viable time to decay
            timeinrun.append(t1)

        av = trail.averagelifetime(timeinrun, numpoints)   #finding each average lifetime
        avtimes.append(av)

    perdiff = ((av - tau)/tau) * 100

    print('The expected tau is 2.2e-6s')
    print('The last average characteristic lifetime was ' + str(av) + ' s')
    print('The percentage difference from the given value is ' + str(perdiff) + ' %')
    pl.hist(timeinrun, bins = 50)   #plots histogram of last run of experiment
    pl.show()
    pl.hist(avtimes, bins = 50)   #plots histogram of average times
    pl.show()

    '''
    The ability to trust this can be worked out mathemtaically. The standard error on this
    is the sigma/((n)^(1/2)), but this must be combined with the error on the expermiment itselfs.
    The first sigma is roughly 34.1% on either side of the centred value for the gaussian.
    '''

main()
