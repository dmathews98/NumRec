'''
Unit 3 Exercise 1 - Bisection Method
'''

'''
Class for Bisect method

n = log_2((x2-x1)/0.00001)
'''

import numpy as np
import math as m

class Bisect(object):

    def __init__(self, xi, xf, epsilon):
        self.x1 = xi
        self.x2 = xf
        self.n = m.log((xf-xi)/epsilon)

    def evalf(self, x):
        fx = 10.2 - 7.4*x -2.1*(x**(2.0)) + x**(3.0)

        return fx

    def evalg(self, x):
        gx = m.exp(x) - 2.0

        return gx

    def evalh(self, x):
        hx = m.cos(x)*m.sin(3*x)

        return hx

    def matcherf(self, x1, x2, xc):
        if self.evalf(x1) >= 0 and self.evalf(xc) >= 0:
            return True
        elif self.evalf(x1) <= 0 and self.evalf(xc) <= 0:
            return True

    def matcherg(self, x1, x2, xc):
        if self.evalg(x1) >= 0 and self.evalg(xc) >= 0:
            return True
        elif self.evalg(x1) <= 0 and self.evalg(xc) <= 0:
            return True

    def matcherh(self, x1, x2, xc):
        if self.evalh(x1) > 0 and self.evalh(xc) > 0:
            return True
        elif self.evalh(x1) < 0 and self.evalh(xc) < 0:
            return True

    def centrex(self, x1, x2):
        xc = x1 + (x2-x1)/2.0

        return xc

    def iterationf(self, x1, x2):
        i = 0
        while i < self.n:
            xc = self.centrex(x1, x2)
            if self.matcherf(x1, x2, xc) == 1:
                x1 = xc
            elif self.matcherf(x1, x2, xc) != 1:
                x2 = xc
            i += 1

        return xc

    def iterationg(self, x1, x2):
        i = 0
        while i < self.n:
            xc = self.centrex(x1, x2)
            if self.matcherg(x1, x2, xc) == 1:
                x1 = xc
            elif self.matcherg(x1, x2, xc) != 1:
                x2 = xc
            i += 1

        return xc

    def iterationh(self, x1, x2):
        i = 0
        while i < self.n:
            xc = self.centrex(x1, x2)
            if self.matcherh(x1, x2, xc) == 1:
                x1 = xc
            elif self.matcherh(x1, x2, xc) != 1:
                x2 = xc
            i += 1

        return xc
