'''
Unit 3 Exercise 1 - Newton-Raphson Method
'''

'''
f(x) = 10.2 - 7.4*x - 2.1*x**(2) + x**(3)

df/dx = -7.4 -4.2*x + 3.0*x**(2.0)

g(x) = m.e**(x) - 2.0

dg/dx = m.e**(x)

h(x) = m.cos(x)*m.sin(3*x)

dh/dx = (3 * m.cos(x) * m.cos((3 * x))) - (m.sin(x) * m.sin((3 * x)))

d = -1 * (f(xo) / f'(xo))
'''

import math as m

class NewtonRaphson(object):

    def __init__(self, x):
        self.xo = x

    def evalf(self, x):
        fx = 10.2 - 7.4*x -2.1*(x**(2.0)) + x**(3.0)

        return fx

    def evaldfdx(self, x):
        dfdx = -7.4 -4.2*x + 3.0*x**(2.0)

        return dfdx

    def evalg(self, x):
        gx = m.exp(x) - 2.0

        return gx

    def evaldgdx(self, x):
        dgdx = m.e**(x)

        return dgdx

    def evalh(self, x):
        hx = m.cos(x)*m.sin(3*x)

        return hx

    def evaldhdx(self, x):
        dhdx = (3 * m.cos(x) * m.cos((3 * x))) - (m.sin(x) * m.sin((3 * x)))

        return dhdx

    def ffindd(self, x):
        d = -1 * (self.evalf(x)/self.evaldfdx(x))

        return d

    def gfindd(self, x):
        d = -1 * (self.evalg(x)/self.evaldgdx(x))

        return d

    def hfindd(self, x):
        d = -1 * (self.evalh(x)/self.evaldhdx(x))

        return d

    def iteratef(self, x, k):
        for i in range(k):
            if self.evalf(x) != 0:
                x = x + self.ffindd(x)

        return x

    def iterateh(self, x, k):
        for i in range(k):
            if self.evalh(x) != 0:
                x = x + self.hfindd(x)

        return x

    def iterateg(self, x, k):
        for i in range(k):
            if self.evalg(x) != 0:
                x = x + self.gfindd(x)

        return x
