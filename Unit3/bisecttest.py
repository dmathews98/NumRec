'''
Test class for Unit 3 - Exercise 1: The Bisection Method
'''

from functions import Functions
from bisectclass import Bisect

def main():

    initx = -4
    finalx = 4
    numpoints = 500
    error = 0.00001
    rootsf = []
    rootsg = []
    rootsh = []

    run = Functions(initx, finalx, numpoints)

    run.plotf() #roots by inspect; [-3, -2], [1, 2], [3, 4]
    run.plotg() #root by inspect; [0, 1]
    run.ploth() #roots by inspec; [-0.5, 0.5], [1, 1.5], [2, 2.5], [3, 3.5]

    bis = Bisect(-3, -2, error)
    rootsf.append(bis.iterationf(-3, -2))
    bis = Bisect(1, 2, error)
    rootsf.append(bis.iterationf(1, 2))
    bis = Bisect(3, 4, error)
    rootsf.append(bis.iterationf(3, 4))

    bis = Bisect(0, 1, error)
    rootsg.append(bis.iterationg(0, 1))

    bis = Bisect(-0.1, 0.1, error)
    rootsh.append(bis.iterationh(-0.1, 0.1))
    bis = Bisect(1, 1.5 , error)
    rootsh.append(bis.iterationh(1, 1.5))
    bis = Bisect(2, 2.5, error)
    rootsh.append(bis.iterationh(2, 2.5))
    bis = Bisect(3, 3.5, error)
    rootsh.append(bis.iterationh(3, 3.5))

    print('The roots of f(x) are ' + str(rootsf))
    print('The roots of g(x) are ' + str(rootsg))
    print('The roots of h(x) are ' + str(rootsh))

main()
