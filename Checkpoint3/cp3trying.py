'''
Checkpoint 3 - s1610357 - Declan Mathews
'''

'''
f is derivative: dy/dx

For this cp f is the charge density

E(x=-2) = 0

Euler:

y(xn) = y(x) + delta*f(y(x), x)

RK4:

k1 = f(x, y)   -   slope at beginning
k2 = f(x + delta/2.0 , y + delta * (k1/2.0))
k3 = f(x + delta/2.0 , y + delta * (k2/2.0))
k4 = f(x + delta/2.0 , y + delta * k3)

y(xn) = y(x) + delta * (k1/6.0 + k2/3.0 + k3/3.0 + k4/6.0)
'''

import numpy as np
from ChargeDistribution import ChargeDistribution as Qdist
import matplotlib.pyplot as pl

#============================ELECTRICFIELD ITERATOR============================#

class ElectricField(object):

    def __init__(self, step, nsteps, inxdata):
        self.rho = Qdist()   #initiating the given class ChargeDistribution
        self.d = step
        self.its = nsteps   #number of iterations
        self.x = inxdata

    '''Does Euler integration'''
    def runeulerE(self):
        y = np.zeros(len(self.x))   #initialises array for output
        y[0] = 0        #first E(x) at x = -2 = 0
        for i in range(1, self.its):
            f = self.rho.evaluate(self.x[i-1])   #increase in E(x)
            y[i] = y[i-1] + self.d * f   #updating next E(x)

        return y

    '''Does RK4 integration'''
    def runrk4E(self):
        y = np.zeros(len(self.x))   #initialises array for output
        y[0] = 0        #first E(x) at x = -2 = 0
        for i in range(1, self.its):
            k1 = self.rho.evaluate(self.x[i-1])
            k2 = self.rho.evaluate(self.x[i-1] + (self.d/2.0))
            k4 = self.rho.evaluate(self.x[i-1] + self.d)

            f = (k1/6.0 + k2/3.0 + k2/3.0 + k4/6.0)   #increase in E(x)
            y[i] = y[i-1] + self.d * f   #updating next E(x)

        return y

#===============================VOLTAGE ITERATOR===============================#

class Voltage(object):

    def __init__(self, step, nsteps, Edata, xdata, limits):
        self.d = step
        self.its = nsteps   #number of iterations
        self.Ex = Edata
        self.lims = limits

    '''Does Euler integration'''
    def runeulerV(self):
        y = np.zeros(len(self.Ex))
        y[0] = 0        #first V(x) at x = -2 = 0
        for i in range(1, self.its):
            f = (-1.0) * self.Ex[i-1]
            y[i] = y[i-1] + (self.d * f)

        return y

    '''Does RK4 integration'''
    def runrk4V(self):
        midx = np.arange(self.lims[0]+(self.d * 0.5), self.lims[1]+(self.d * 0.5), self.d)   #finds mid x for k2 and 3
        formid = ElectricField(self.d, self.its, midx)   #initialises e field class for midx
        Emid = formid.runrk4E()   #returns E(x) for mid values and then *-1
        y = np.zeros(len(self.Ex))   #initialises output
        y[0] = 0   #V(x=-2) = 0
        for i in range(self.its):
            k1 = (-1.0) * self.Ex[i-1]
            k2 = (-1.0) * Emid[i-1]
            k4 = (-1.0) * self.Ex[i]

            dy = self.d * (k1/6.0 + k2/3.0 + k2/3.0 + k4/6.0)
            y[i] = y[i-1] + dy

        return y

#================================PLOT RESULTS==================================#

class Graphing(object):

    def __init__(self, e, r, x):
        self.x = x
        self.ye = e   #y euler
        self.yr = r   #y rk4

    '''Plots E(x) vs x graph'''
    def plotE(self):
        pl.plot(self.x, self.ye, 'r')
        pl.plot(self.x, self.yr, 'g')
        pl.title('E(x) ; Red Euler ; Green RK4')
        pl.show()

    '''Plots V(x) vs x graph'''
    def plotV(self):
        pl.plot(self.x, self.ye, 'r')
        pl.plot(self.x, self.yr, 'g')
        pl.title('V(x) ; Red Euler ; Green RK4')
        pl.show()

#=========================INITIAL PARAMTER FINDING=============================#

class params(object):

    def __init__(self, limits, delta):
        self.delta = delta
        self.lims = limits

    '''Finds number of steps to perform'''
    def findnumsteps(self):
        nsteps = int((self.lims[1]-self.lims[0])/self.delta)
        return nsteps

    '''Finds the x data for given delta'''
    def findinitxdata(self, nsteps):
        initxdata = np.arange(self.lims[0], self.lims[1], self.delta)
        return initxdata

#===============================MAIN FUNCTION==================================#

def main():
    '''Hardcoded data'''
    limits = [-2.0, 2.0]
    delta = 0.05

    '''Finds initial data and number of steps'''
    finding = params(limits, delta)
    nsteps = finding.findnumsteps()
    inxdata = finding.findinitxdata(nsteps)

    '''Euler E(x)'''
    Ee = ElectricField(delta, nsteps, inxdata)
    eulerEdata = Ee.runeulerE()

    '''RK4 E(x)'''
    Er = ElectricField(delta, nsteps, inxdata)
    rk4Edata = Er.runrk4E()

    '''Plot of Euler and RK4 E(x) vs x'''
    Eplot = Graphing(eulerEdata, rk4Edata, inxdata)
    Eplot.plotE()

    '''Euler V(x)'''
    Ve = Voltage(delta, nsteps, eulerEdata, inxdata, limits)
    eulerVdata = Ve.runeulerV()

    '''RK4 V(x)'''
    Vr = Voltage(delta, nsteps, rk4Edata, inxdata, limits)
    rk4Vdata = Vr.runrk4V()

    '''Plot of Euler and RK4 V(x) vs x'''
    Vplot = Graphing(eulerVdata, rk4Vdata, inxdata)
    Vplot.plotV()

main()
