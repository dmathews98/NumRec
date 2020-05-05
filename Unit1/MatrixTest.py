'''
Tests the matrix class without numpy
'''

from Matrix import MyMatrix

def main():

    Arows = input('How many rows in A? ')
    Acol = input('How many columnsin A? ')

    A = MyMatrix(Arows, Acol)

    for i in range(Arows):
        for j in range(Acol):
            num = input('Enter values in English reading order for A: ')
            A.setval(num, i, j)

    A.printmat(Arows, Acol)

    Brows = input('How many rows in B? ')
    Bcol = input('How many columnsin B? ')

    B = MyMatrix(Brows, Bcol)

    for i in range(Brows):
        for j in range(Bcol):
            num = input('Enter values in English reading order for B: ')
            B.setval(num, i, j)

    B.printmat(Brows, Bcol)

    if A.addcheck(Arows, Acol, Brows, Bcol) == 1:
        print('A + B')
        C = A.addmats(Arows, Acol, B)
        C.printmat(Arows, Acol)
    else:
        print('Cant add\n')

    if A.multicheck(Arows, Acol, Brows, Bcol) == 1:
        print('A * B')
        D = A.multimats(Arows, Acol, Brows, Bcol, B)
        D.printmat(Brows, Bcol)
    else:
        print('Cants multiply\n')

main()
