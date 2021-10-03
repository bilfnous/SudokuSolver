#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "sudoku_model.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Mar/2020"


# Creates 2D array that contains 9 lists, each of 9 items, all set to 0 
grid_m = [[0 for i in range(9)] for i in range(9)]

def read_grid(grid):
    print("Fill in the sudoku grid; enter 0 to fill the empty cell: ")
    for i in range(9):
        for j in range(9):
            grid[i][j] = input(f'[{i + 1}] [{j + 1}] >> ')


# return possible numbers for each index

def solve_row():

    return 0

def sovle_colmun():

    return 0

def solve_square():

    return 0