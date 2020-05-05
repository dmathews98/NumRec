'''
Checkpoint 2 chi squared minimisation - s1610357 Declan Mathews
'''

'''
y = m*x + c
di**2 = ((ym - yp)/epsilon)**2
chisqr = sum of di**2 for i = 1 -> numpoints
'''

import numpy as np
from scipy import optimize as sc
from scipy.interpolate import interp1d
import matplotlib.pyplot as pl

################################################################################
#                              ChiSq Minimiser Class                           #
################################################################################
class ChiSqMinimiser(object):

    '''Constructor initialisd with data from txt file and initialised values to be minimised'''
    def __init__(self):
        self.var = np.loadtxt('testdata.txt')
        self.mingrad = 0  #these are initialised for storing the values found through minimisation
        self.minc = 0
        self.minchi = 0

    '''Prints minimised gradient'''
    def retmingrad(self):
        print('The minimised gradient is ' + str(self.mingrad))
        #roughly -0.0028
        return self.mingrad

    '''Prints minimised c value'''
    def retminc(self):
        print('The minimised c value is ' + str(self.minc))
        #roughly 0.995
        return self.minc

    '''Returns minimum chisq value'''
    def retminchi(self):
        return self.minchi

    '''Finds predicted y value for given m and c(as array) and returns as array'''
    def StraightLine(self, x):
        return self.var[:,0]*x[0] + x[1]   #predicted y values of straight line

    '''Function for finding Chi Squared'''
    def Chisq(self, x):
        chisq = 0   #initialised for summation
        yp = self.StraightLine(x)   #finds predicted y values
        disq = ((self.var[:,1] - yp)/self.var[:,2])**2.0   #dsquared values
        for i in range(len(disq)):   #Done over all data in column
            chisq += disq[i]   #summed dsqr for chisq

        return chisq

    '''Minimiser function from ScyPy, min values stored'''
    def minimiser(self, x):
        minval = sc.minimize(self.Chisq, x, method = 'Nelder-Mead')   #minimised values
        self.mingrad = minval.x[0]
        self.minc = minval.x[1]
        self.minchi = minval.fun

################################################################################
#            Gets m, c and chi data and plots graphs, also finds error         #
#                            on minimised m and c                              #
################################################################################
class ChiData(object):

    '''Constructor, creates stacked array of m and c data'''
    def __init__(self, mdata, cdata, points, minim, minic, minichisq):
        self.m = mdata
        self.c = cdata
        self.p = points
        self.minm = minim
        self.minc = minic
        self.minchi = minichisq

        self.passdata = np.column_stack((mdata, cdata))    #stacked into array for single pass into chisq
        self.chidata = np.array([])    #array for calculcated chisq

    '''Calculating chisq and appending to list for plotting'''
    def gatherchi(self):
        foo = ChiSqMinimiser()
        for i in range(self.p):
            chi = foo.Chisq(self.passdata[i])
            self.chidata = np.append(self.chidata, chi)

    '''Plots m data v chisq and determiens error or m'''
    def mplot(self):
        pl.plot(self.m, self.chidata)
        pl.title('m v chi squared')
        pl.xlabel('m')
        pl.ylabel('chi squared')
        axes = pl.gca()
        axes.set_xlim([-0.045, 0.04])
        axes.set_ylim([0, 1500])
        m1 = interp1d(self.chidata, self.m, fill_value = 'extrapolation')   #sets function for x at y
        dm = np.absolute(self.minm - m1(self.minchi + 1.0))    #determines error by difference in m at min chi and 1 unit chi
        print('The error on m is +/- ' + str(dm))
        pl.show()

    '''Plots c data v chisq and determines error on c'''
    def cplot(self):
        pl.plot(self.c, self.chidata)
        pl.title('c v chi squared')
        pl.xlabel('c')
        pl.ylabel('chi squared')
        axes = pl.gca()
        axes.set_xlim([0.975, 1.02])
        axes.set_ylim([0,1500])
        c1 = interp1d(self.chidata, self.c, fill_value = 'extrapolation')   #sets function for x at y
        dc = np.absolute(self.minc - c1(self.minchi + 1))   #determines error by difference in c at min chi and 1 unit chi
        print('The error on c is +/- ' + str(dc))
        pl.show()


################################################################################
#                               MAIN FUNCTION                                  #
################################################################################
def main():
    '''Initial Data - Here for hard coding'''
    variables = np.array([0.1, 1])   # m, c first guess
    points = 500   #number of points for graphs
    mdata = np.linspace(-0.2, 0.2, points)   #spread of m data for graphs
    cdata = np.linspace(0.9, 1.1, points)    #spread of c data for graphs

    '''Initialising, running and printing of minimiser and its values'''
    run = ChiSqMinimiser()
    run.minimiser(variables)
    mingrad = run.retmingrad()   #minimum m value
    minc = run.retminc()   #minimum c value
    minichisq = run.retminchi()   #minimum chi value

    '''Initialising, running and printing of Chidata for m and c and their graphs'''
    init = ChiData(mdata, cdata, points, mingrad, minc, minichisq)
    init.gatherchi()
    init.mplot()
    init.cplot()

main()
