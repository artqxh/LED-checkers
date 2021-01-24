import numpy as np

A = np.array([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 0, 1, 0]
                ])
a4 = A[0,0]
b4 = A[0,1]
c4 = A[0,2]
d4 = A[0,3]

a3 = A[1,0]
b3 = A[1,1]
c3 = A[1,2]
d3 = A[1,3]

a2 = A[2,0]
b2 = A[2,1]
c2 = A[2,2]
d2 = A[2,3]

a1 = A[3,0]
b1 = A[3,1]
c1 = A[3,2]
d1 = A[3,3]

print(A)

number, move = input("Enter a number of checker and move(l/r): ").split()


B = np.array([['a4', 'b4', 'c4', 'd4'],
              ['a3', 'b3', 'c3', 'd3'],
              ['a2', 'b2', 'c2', 'd2'],
              ['a1', 'b1', 'c1', 'd1']
              ])



for i, x in enumerate(B):
    for j, y in enumerate(x):
        if number in y:
            if move == 'l':
                if j > 0:
                    A[i, j] = 0
                    i = i - 1
                    j = j - 1
                    A[i, j] = 1
                    print(A)
                else:
                    print('Wrong direction')
            elif move == 'r':
                if j < 3:
                    A[i, j] = 0
                    i = i - 1
                    j = j + 1
                    A[i, j] = 1
                    print(A)
                else:
                    print('Wrong direction')
            else:
                print('Wrong direction')

