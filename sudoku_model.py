#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "sudoku_model.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Mar/2020"

ROW_COL_LEN = 9
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
            if var in NUMBERS:
                possible.remove(var)
    return possible

# return possible numbers for each index in a colmun
def sovle_colmun(grid, col, possible):
    for i in range(ROW_COL_LEN):
        if grid[i][col] != 0:
            var = int(grid[i][col])
            if var in NUMBERS:
                possible.remove(var)
    return possible

# return possible numbers for each index in a square
def solve_square(grid, row, col, possible):
    for i in range(3):
        for j in range(3):
               if grid[row + i][col + j] != 0:
                   var = int(grid[row + i][col + j])
                   if var in NUMBERS:
                       possible.remove(var)    
    return possible

# return possible numbers for each index in a neighbouring rows (the row before and after the index in quary)
def neighbour_row(possible):

    return possible

# return possible numbers for each index in a neighbouring colmuns (the columns above and below the index in quary)
def neighbour_colmun(possible):

    return possible