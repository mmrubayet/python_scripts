import numpy as np

def check_sudoku(grid):

    for i in range(9):
        # j, k index top left hand corner of each 3x3 tile
        j, k = (i // 3) * 3, (i % 3) * 3
        if len(set(grid[i,:])) != 9 or len(set(grid[:,i])) != 9\
                   or len(set(grid[j:j+3, k:k+3].ravel())) != 9:
            return False
    return True

data = []

for i in range(9):
    data.append(list(map(int, input())))
grid = np.array(data)

if check_sudoku(grid):
    print('Yes')
else:
    print('No')
