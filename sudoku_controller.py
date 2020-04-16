#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __auther__ B. Alfanous
# __email__ b.alfanous@outlook.com
# __date__ 28/Mar/2020
# __file__ sudoku_controller.py

def read_grid(grid):
    print("Fill in the sudoku grid; enter 0 to fill the empty square: ")
    for i in range(9):
        for j in range(9):
            grid[i][j] = input(f'[{i + 1}] [{j + 1}] >> ')