#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __auther__ B. Alfanous
# __email__ b.alfanous@outlook.com
# __date__ 28/Mar/2020
# __file__ sudoku_model.py

import sudoku_controller as controller
import sudoku_view as view

grid_m = [[0 for i in range(9)] for i in range(9)]
possibilties_m = [[ [] for i in range(9)] for i in range(9)]

def solve_grid():
    for row in range(9):
        for col in range(9):
            if grid_m[row][col] == 0 :
                possibilties_m[row][col] = get_possibilties(row, col)

def get_possibilties(row, col):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if grid_m[row][i] != 0:
            if grid_m[row][i] in numbers:
                numbers.remove(grid_m[row][i])
        
        if grid_m[i][col] != 0:
            if grid_m[i][col] in numbers:
                numbers.remove(grid_m[i][col])


    return numbers


def main():
    controller.read_grid(grid_m)
    solve_grid()
    view.print_grid(grid_m)
            
if __name__ == '__main__': main()