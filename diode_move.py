import numpy as np

A = np.array([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 0, 1, 0]
                ])

print(A)

B = np.array([['a4', 'b4', 'c4', 'd4'],
              ['a3', 'b3', 'c3', 'd3'],
              ['a2', 'b2', 'c2', 'd2'],
              ['a1', 'b1', 'c1', 'd1']])
print(B)

# taking two inputs at a time
x, y = input("Enter a number and move(l/r): ").split()

if y == 'l':
    print('left')
if y == 'r':
    print('right')
else:
    print('Wrong move')

#print("Number of checker: ", x)
#print("Move: ", y)
print()