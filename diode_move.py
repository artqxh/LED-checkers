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

if move == 'l':
    print('left')
elif move == 'r':
    print('right')
else:
    print('Wrong move')


print()
if number == 'b1' and move == 'l':
    b1 = a2
elif number == 'b2' and move == 'r':
    b1 = c2


B = np.array([['a4', 'b4', 'c4', 'd4'],
              ['a3', 'b3', 'c3', 'd3'],
              ['a2', 'b2', 'c2', 'd2'],
              ['a1', 'b1', 'c1', 'd1']])



for i, x in enumerate(B):
    for j, y in enumerate(x):
        if number in y:
            print(i, j)



if 1 == 1:
    if move == 'l':
        A[i, j]
        print(A[i-1, j-1])
    elif move == 'r':
        A[i,j]
        print(A[i-1, j+1])
else:
    print('Wrong combination')


print(A)