'''
Checkpoint 2 - Negative Log Likelihood of Muon Decays
'''

'''
tau = 2.2e-6
lmda = 1/tau
L = product sum of t = (lmda)*exp(-(lmda)/tau)
nll = -log(L)

t.f. nll = sum -log(Li)
'''

import math as m
import numpy as np
from scipy import optimize as  sc
from scipy.interpolate import interp1d
import matplotlib.pyplot as pl
from muonmontecarlonohist import MuonDecay

################################################################################
#                      CLASS FOR GATHERING DECAY TIME DATA                     #
################################################################################

class gathertimes(object):

    '''Constructor'''
    def __init__(self, tauval, points):
        self.tdata = np.array([])
        self.tau = tauval
        self.lmda = 1.0 / tauval   #lambda
        self.decays = points   #number of decays

    '''Gathers data using MuonDecay Class'''
    def fetch(self):
        for i in range(self.decays):
            trail = MuonDecay(self.tau)
            t1 = trail.evaluate()

            self.tdata = np.append(self.tdata, t1)

        return self.tdata

################################################################################
#                             NLL MINIMISER CLASS                              #
################################################################################

class nllminimiser(object):

    '''Constructor'''
    def __init__(self, times, tauval):
        self.tdata = times
        self.tau = tauval
        self.nllmin = 0
        self.tmin = 0

    '''Returns minimum nll'''
    def retnllmin(self):
        return self.nllmin

    '''Prints and returns time min'''
    def rettmin(self):
        print('The minimum value of t is ' + str(self.tmin) + ' s')
        return self.tmin

    '''Equation to find nll'''
    def findnll(self, t):
        return np.log(t) + (self.tdata / t)

    '''Function for minimising nll'''
    def nllcalc(self, t):
        nll = 0   #resets to 0 for summing
        nllset = self.findnll(self.tau)
        nllguess = self.findnll(t)
        dsq = (nllset - nllguess)**2.0
        for i in range(len(dsq)):
            nll += dsq[i]

        return nll

    '''Minimising class, using scipy'''
    def minimiser(self, t):
        minval = sc.minimize(self.nllcalc, t)
        self.tmin = minval.x[0]
        self.nllmin = minval.fun
        print(minval)

################################################################################
#              GATHERS NLL DATA, PLOTS GRAPH AND CALCULATES ERROR              #
################################################################################

class nlldata(object):

    '''Constructor'''
    def __init__(self, tdata, tauval, taulist, numpoints, minit, mininll):
        self.t = tdata
        self.tau = tauval
        self.taudata = taulist
        self.p = numpoints
        self.mint = minit
        self.minnll = mininll

        self.nlldata = np.array([])

    '''Gathers nll data for plotting'''
    def gathernll(self):
        foo = nllminimiser(self.t, self.tau)
        for i in range(self.p):
            self.nlldata = np.append(self.nlldata, foo.nllcalc(self.taudata[i]))

    '''Plots graph of nll against t'''
    def nllplot(self):
        pl.plot(self.taudata, self.nlldata)
        pl.show()

################################################################################
#                               MAIN FUNCTION                                  #
################################################################################

def main():
    '''Hardcoded quantities and variables'''
    tau = 2.2e-6
    numdecays = 1000
    guess = 2.0e-6
    taudata = np.linspace(2.0e-6, 2.4e-6, numdecays)

    '''Gathers decay times'''
    trail = gathertimes(tau, numdecays)
    tdata = trail.fetch()

    '''Runs minimiser and finds minimum values'''
    run = nllminimiser(tdata, tau)
    run.minimiser(guess)
    minnll = run.retnllmin()
    mint = run.rettmin()

    '''Gathers data, plots graphs and finds error'''
    init = nlldata(tdata, tau, taudata, numdecays, mint, minnll)
    init.gathernll()
    init.nllplot()

main()
