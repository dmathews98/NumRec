'''
Unit 3 Functions Class
'''

'''
Class for the functions and their evaluation

f(x) = 10.2 - 7.4x - 2.1x**(2) + x**(3)

g(x) = m.e^(x) - 2.0

h(x) = m.cos(x)*m.sin(3*x)
'''

import math as m
import numpy as np
import matplotlib.pyplot as pl

class Functions(object):

    def __init__(self, xi, xf, numpoints):
        self.xdata = np.linspace(xi, xf, numpoints)

    def evalf(self, x):
        fx = 10.2 - 7.4*x -2.1*(x**(2.0)) + x**(3.0)

        return fx

    def evalg(self, x):
        gx = m.exp(x) - 2.0

        return gx

    def evalh(self, x):
        hx = m.cos(x)*m.sin(3*x)

        return hx

    def gatherf(self):
        fx1 = []
        for i in range(len(self.xdata)):
            fx1.append(self.evalf(self.xdata[i]))

        return fx1

    def gatherg(self):
        gx1 = []
        for i in range(len(self.xdata)):
            gx1.append(self.evalg(self.xdata[i]))

        return gx1

    def gatherh(self):
        hx1 = []
        for i in range(len(self.xdata)):
            hx1.append(self.evalh(self.xdata[i]))

        return hx1

    def plotf(self):
        fplotdata = self.gatherf()

        pl.plot(self.xdata, fplotdata)
        pl.title('f(x) blue')
        pl.axhline(y=0, color='r')
        pl.axvline(x=0, color='r')
        pl.grid(True)
        pl.show()

    def plotg(self):
        gplotdata = self.gatherg()

        pl.plot(self.xdata, gplotdata, 'g')
        pl.title('g(x) green')
        pl.axhline(y=0, color='r')
        pl.axvline(x=0, color='r')
        pl.grid(True)
        pl.show()

    def ploth(self):
        hplotdata = self.gatherh()

        pl.plot(self.xdata, hplotdata, 'k')
        pl.title('h(x) black')
        pl.axhline(y=0, color='r')
        pl.axvline(x=0, color='r')
        pl.grid(True)
        pl.show()
