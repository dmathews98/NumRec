'''
Checkpoint 2 - Negative Log Likelihood of Muon Decays - s1610357 Declan Mathews
'''

'''
tau = 2.2e-6
lmda = 1/tau
L = product sum of t = (lmda)*exp(-(lmda)/tau)
nll = -log(L)

t.f. nll = sum -log(Li)
'''

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
        self.tau = tauval   #true value of tau
        self.nllmin = 0
        self.tmin = 0

    '''Returns minimum nll'''
    def retnllmin(self):
        return self.nllmin

    '''Prints and returns time min'''
    def rettmin(self):
        print('The minimum value of t is ' + str(self.tmin) + ' s')
        #Values about 2.15e-6s - 2.25e-6s fo 10000 and 2e-6s - 2.3e-6s for 1000
        return self.tmin

    '''Equation to find -log(L) for each decay at tau'''
    def findnll(self, t):
        return np.log(t) + (self.tdata / t)

    '''Function for finding nll'''
    def nllcalc(self, t):
        nll = 0   #resets to 0 for summing
        nllset = self.findnll(t)
        for i in range(len(nllset)):
            nll += nllset[i]

        return nll

    '''Minimising function, using scipy'''
    def minimiser(self, t):
        minval = sc.minimize(self.nllcalc, t, method = 'Nelder-Mead')
        self.tmin = minval.x[0]
        self.nllmin = minval.fun

################################################################################
#              GATHERS NLL DATA, PLOTS GRAPH AND CALCULATES ERROR              #
################################################################################
class nlldata(object):

    '''Constructor'''
    def __init__(self, tdata, taudat, tauval, numpoints, minit, mininll):
        self.t = tdata
        self.tau = taudat   #tau list for attempts at nll
        self.tautrue = tauval   #tru tau val
        self.p = numpoints   #numdecays corresponds to num of data points
        self.mint = minit
        self.minnll = mininll

        self.nlldata = np.array([])   #initialise array for nll for plotting

    '''Gathers nll data for plotting'''
    def gathernll(self):
        foo = nllminimiser(self.t, self.tautrue)
        for i in range(self.p):
            self.nlldata = np.append(self.nlldata, foo.nllcalc(self.tau[i]))

    '''Plots graph of nll against t'''
    def nllplot(self):
        pl.plot(self.tau, self.nlldata)
        pl.title('tau v nll')
        pl.xlabel('tau')
        pl.ylabel('nll')
        axes = pl.gca()
        axes.set_xlim([2.0e-6, 2.40e-6])
        #axes.set_ylim([-12040, -12000])   #this can be used to zoom in
        t1 = interp1d(self.nlldata, self.tau, fill_value = 'extrapolation')   #sets func for x at y
        dt = np.absolute(self.mint - t1(self.minnll + 0.5))   #finds t at 0.5 above minnll, which is error on t
        print('The error on tau is +/- ' + str(dt) + ' s')
        #Values about 1e-8s - 1e-10s for 1000 and 10000, however
        #for 1000 it mostly is in the e-8 while for 10000 is e-9
        pl.show()

################################################################################
#                               MAIN FUNCTION                                  #
################################################################################
def main():
    '''Hardcoded quantities and variables'''
    tau = 2.2e-6
    numdecays = 1000
    tauguess = 2.0e-6
    taudata = np.linspace(2.0e-6, 2.4e-6, numdecays)

    '''Gathers decay times'''
    trail = gathertimes(tau, numdecays)
    tdata = trail.fetch()

    '''Runs minimiser and finds minimum values'''
    run = nllminimiser(tdata, tau)
    run.minimiser(tauguess)
    minnll = run.retnllmin()   #min nll value
    mint = run.rettmin()   #min tau value

    '''Gathers data, plots graphs and finds error'''
    init = nlldata(tdata, taudata, tau, numdecays, mint, minnll)
    init.gathernll()
    init.nllplot()

main()
