'''
Class for defining Matrix without numpy
'''

class MyMatrix(object):

    def __init__(self, m, n):
        self.mrx = [0] * m
        for i in range(m):
            self.mrx[i] = [0] * n

    def setval(self, x, m, n):
        self.mrx[m][n] = x

    def addcheck(self, m, n, i, j):
        if m == i and n == j:
            return 1

    def addmats(self, m, n, b):
        c = MyMatrix(m, n)
        for i in range(m):
            for j in range(n):
                c.mrx[i][j] = self.mrx[i][j] + b.mrx[i][j]

        return c

    def multicheck(self, m, n, i, j):
        if m == j and n == i:
            return 1

    def multimats(self, m, n, o, p, b):
        result = MyMatrix(o, p)
        # iterate through rows of A
        for i in range(m):
            # iterate through columns of B
            for j in range(p):
                # iterate through rows of B
                for k in range(o):
                    result.mrx[i][j] += self.mrx[i][k] * b.mrx[k][j]

        return result

    def printmat(self, m, n):
        prmtrx = str('\n')
        for i in range(m):
            for j in range(n):
                prmtrx += str(self.mrx[i][j]) + str(' ')
            prmtrx += str('\n')
        print(prmtrx)
