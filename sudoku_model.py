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
            grid[i][j] = input(f'[{i + 1}] [{j + 1}] >> ')


# return possible numbers for each index

def solve_row(grid, row):
    possible = NUMBERS

    for i in range(ROW_COL_LEN):
        if grid[row][i] != 0:
            var = grid[row][i]
            for j in range(ROW_COL_LEN):
                if var == NUMBERS[j]:
                    possible.remove(j)
    return possible


def sovle_colmun():

    return 0

def solve_square():

    return 0

def neighbour_row():

    return 0

def neighbour_colmun():

    return 0