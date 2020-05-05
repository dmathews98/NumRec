'''
Test file for Checkpoint 1 - Muon Decay by MonteCarlo
'''

import numpy as np
import matplotlib.pylab as pl
from muonmontecarlonohist import MuonDecay

def main():

    '''Sets values for easy changing in hard code'''
    tau = 2.2e-6   #characteristic lifetime
    numpoints = 1000   #number of decay times to be recorded
    avtimes = []   #average lifetime per run stored here
    runs = 500   #number of experiment repetions
    timeinrun = []   #average characteristic time per experiment

    '''Loop for each run of experiment'''
    for k in range(runs):
        trail = MuonDecay(tau)   #initialises class, repeated for each experiment to reset
        avt = trail.repetitions(numpoints)

        avtimes.append(avt)

    perdiff = ((avt - tau)/tau) * 100   #percentage difference 1 av

    avav = trail.averagelifetime(avtimes, runs)
    perdiff2 = ((avav - tau)/tau) * 100   #percentage difference all avs

    print('The expected tau is 2.2e-6s')
    print('The last average characteristic lifetime was ' + str(avt) + ' s')
    print('The percentage difference from the given value is ' + str(perdiff) + ' %')
    print('The mean of the average times is ' + str(avav) + ' s')
    print('The percentage difference from the given value is ' + str(perdiff2) + ' %')

    pl.hist(avtimes, bins = 50)   #plots histogram of average times
    pl.show()

    '''
    The ability to trust this can be worked out mathemtaically. The standard error on this
    is the sigma/((n)^(1/2)), but this must be combined with the error on the expermiment itselfs.
    The first sigma is roughly 34.1% on either side of the centred value for the gaussian.
    '''

main()
