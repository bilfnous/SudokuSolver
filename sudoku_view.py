#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __auther__ B. Alfanous
# __email__ b.alfanous@outlook.com
# __date__ 28/Mar/2020
# __file__ sudoku_view.py


def print_grid(grid):
    print("- - - - - - - - - - - - - - - - -")
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - -")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" |  ", end="")

            if j == 8:
                print(str(grid[i][j]) + " ")
            else:
                print(str(grid[i][j]) + "  ", end="")
    
    print("- - - - - - - - - - - - - - - - -")