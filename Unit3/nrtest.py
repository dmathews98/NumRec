'''
Class for testing Newton-Raphson method
'''

from functions import Functions
from newtonraphson import NewtonRaphson

def main():

    initx = -4
    finalx = 4
    numpoints = 500
    error = 0.00001
    rootsf = []
    rootsg = []
    rootsh = []

    run = Functions(initx, finalx, numpoints)

    run.plotf() #roots by inspect; -2.5, 1.2, 3.4
    run.plotg() #root by inspect; 0.7
    run.ploth() #roots by inspect; 0, 1.0, 2.1, 3.1

    nr = NewtonRaphson(1)
    rootsf.append(nr.iteratef(-2.5, 500))
    rootsf.append(nr.iteratef(1.2, 500))
    rootsf.append(nr.iteratef(3.4, 500))

    rootsg.append(nr.iterateg(0.7, 500))

    rootsh.append(nr.iterateh(0.1, 500))
    rootsh.append(nr.iterateh(1.0, 500))
    rootsh.append(nr.iterateh(2.1, 500))
    rootsh.append(nr.iterateh(3.1, 500))

    print('The roots of f(x) are ' + str(rootsf))
    print('The roots of g(x) are ' + str(rootsg))
    print('The roots of h(x) are ' + str(rootsh))

main()
