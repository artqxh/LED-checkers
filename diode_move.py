import numpy as np

A = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0]
                ])
a8 = A[0,0]
b8 = A[0,1]
c8 = A[0,2]
d8 = A[0,3]
e8 = A[0,4]
f8 = A[0,5]
g8 = A[0,6]
h8 = A[0,7]

a7 = A[1,0]
b7 = A[1,1]
c7 = A[1,2]
d7 = A[1,3]
e7 = A[1,4]
f7 = A[1,5]
g7 = A[1,6]
h7 = A[1,7]

a6 = A[2,0]
b6 = A[2,1]
c6 = A[2,2]
d6 = A[2,3]
e6 = A[2,4]
f6 = A[2,5]
g6 = A[2,6]
h6 = A[2,7]

a5 = A[3,0]
b5 = A[3,1]
c5 = A[3,2]
d5 = A[3,3]
e5 = A[3,4]
f5 = A[3,5]
g5 = A[3,6]
h5 = A[3,7]

a4 = A[4,0]
b4 = A[4,1]
c4 = A[4,2]
d4 = A[4,3]
e4 = A[4,4]
f4 = A[4,5]
g4 = A[4,6]
h4 = A[4,7]

a3 = A[5,0]
b3 = A[5,1]
c3 = A[5,2]
d3 = A[5,3]
e3 = A[5,4]
f3 = A[5,5]
g3 = A[5,6]
h3 = A[5,7]

a2 = A[6,0]
b2 = A[6,1]
c2 = A[6,2]
d2 = A[6,3]
e2 = A[6,4]
f2 = A[6,5]
g2 = A[6,6]
h2 = A[6,7]

a1 = A[7,0]
b1 = A[7,1]
c1 = A[7,2]
d1 = A[7,3]
e1 = A[7,4]
f1 = A[7,5]
g1 = A[7,6]
h1 = A[7,7]

B = np.array([['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
              ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
              ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
              ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
              ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
              ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
              ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
              ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
              ])

print(A)

while A[0,0] == 0 and A[0,1] == 0 and A[0,2] == 0 and A[0,3] == 0 and A[0,4] == 0 and A[0,5] == 0 and A[0,6] == 0 and A[0,7] == 0:
    number, move = input("Enter a number of checker and move(l/r): ").split()
    for i, x in enumerate(B):
        for j, y in enumerate(x):
            if number in y:
                if move == 'l':
                    if j > 0 and A[i-1, j-1] == 0:
                        A[i, j] = 0
                        A[i-1, j-1] = 1
                        print(A)
                    elif j > 1 and A[i-1, j-1] == 2:
                        A[i, j] = 0
                        A[i-1, j-1] = 0
                        A[i-2, j-2] = 1
                        print(A)
                    else:
                        print('Wrong direction')

                elif move == 'r':
                    if j < 7 and A[i-1, j+1] == 0:
                        A[i, j] = 0
                        A[i-1, j+1] = 1
                        print(A)
                    elif j < 6 and A[i-1, j+1] == 2:
                        A[i, j] = 0
                        A[i-1, j+1] = 0
                        A[i-2, j+2] = 1
                        print(A)

                    else:
                        print('Wrong direction')

                else:
                    print('Wrong direction')