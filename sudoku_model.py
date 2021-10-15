#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "sudoku_model.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Mar/2020"

ROW_COL_LEN = 9
SQUARE_LEN = 3
NUMBERS = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9]

# Creates 2D array that contains 9 lists, each of 9 items, all set to 0 
grid_m = [[0 for i in range(ROW_COL_LEN)] for i in range(ROW_COL_LEN)]

def read_grid(grid):
    print("Fill in the sudoku grid; enter 0 to fill the empty cell: ")
    for i in range(ROW_COL_LEN):
        for j in range(ROW_COL_LEN):
            grid[i][j] = input(f'[{i + 1}] [{j + 1}] >> ') or 0


# return possible numbers for each index in a row
def solve_row(grid, row, possible):
    for i in range(ROW_COL_LEN):
        if grid[row][i] != 0:
            var = int(grid[row][i])
            # replace existing numbers with 0
            if var in possible:
                possible.remove(var)
    return possible

# return possible numbers for each index in a colmun
def sovle_colmun(grid, col, possible):
    for i in range(ROW_COL_LEN):
        if grid[i][col] != 0:
            var = int(grid[i][col])
            if var in possible:
                possible.remove(var)
    return possible

# return possible numbers for each index in a square
def solve_square(grid, row, col, possible):
   row = (row // 3) * 3
   col = (col // 3) * 3
   for i in range(SQUARE_LEN):
       for j in range(SQUARE_LEN):
           if grid[row + i][col + j] != 0:
               var = int(grid[row + i][col + j])
               if var in possible:
                   possible.remove(var)
   return possible

# return possible numbers for each index in a neighbouring rows (the row before and after the index in quary)
def neighbour_row(grid, row, possible):
    exsit = 0
    rtn = [0]
    if row == 0 or row == 3 or row == 6:
        row1 = row + 1
        row2 = row + 2
    elif row == 1 or row == 4 or row == 7:
        row1 = row - 1
        row2 = row + 1
    elif row == 2 or row == 5 or row == 8:
        row1 = row - 1
        row2 = row - 2

    for x in range(len(possible)):
        var = possible[x]
        exsit = 0
        for i in range(ROW_COL_LEN):
            if grid[row1][i] == var:
                exsit += 1
        for j in range(ROW_COL_LEN):
            if grid[row2][j] == var:
                exsit += 1
        if exsit == 2:
            rtn[0] = var
            return rtn
    return possible
    
# return possible numbers for each index in a neighbouring colmuns (the columns above and below the index in quary)
def neighbour_colmun(grid, col, possible):
    exsit = 0
    rtn = [0]
    if col == 0 or col == 3 or col == 6:
        col1 = col + 1
        col2 = col + 2
    elif col == 1 or col == 4 or col == 7:
        col1 = col - 1
        col2 = col + 1
    elif col == 2 or col == 5 or col == 8:
        col1 = col - 1
        col2 = col - 2

    for x in range(len(possible)):
        var = possible[x]
        exsit = 0
        for i in range(ROW_COL_LEN):
            if grid[i][col1] == var:
                exsit += 1
        for j in range(ROW_COL_LEN):
            if grid[j][col2] == var:
                exsit += 1
        if exsit == 2:
            rtn[0] = var
            return rtn
    return possible

# if there are no 0's in the grid, the function returns True, otherwise it returns False
def solved(grid):
    for i in range(ROW_COL_LEN):
        for j in range(ROW_COL_LEN):
            if grid[i][j] == 0:
                return False     
    return True