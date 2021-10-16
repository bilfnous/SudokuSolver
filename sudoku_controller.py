#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "sudoku_controller.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Mar/2020"

import sudoku_model as model
import sudoku_view as view


def main():
    possible = model.NUMBERS
    view.print_grid(model.grid_m)
   # model.read_grid(model.grid_m)
    
    #'''
    model.grid_m = [
        [2, 1, 9, 0, 4, 6, 0, 3, 0],
        [0, 0, 5, 1, 0, 0, 0, 0, 0],
        [0, 3, 4, 0, 0, 0, 2, 6, 0],
        [0, 2, 6, 0, 0, 7, 5, 0, 3],
        [0, 0, 1, 0, 9, 0, 0, 0, 7],
        [4, 7, 3, 0, 6, 5, 0, 0, 8],
        [0, 6, 0, 4, 0, 2, 3, 1, 0],
        [3, 4, 0, 0, 0, 0, 7, 8, 0],
        [1, 0, 0, 0, 0, 0, 4, 5, 0]
    ]
    #'''
    
    view.print_grid(model.grid_m)
    print("\nSearching for a solution...\n")
    counter = 0
    while(model.solved(model.grid_m) != True):
        counter += 1
        if counter == 100:
            break
        print(counter)
        for i in range(model.ROW_COL_LEN):
            for j in range(model.ROW_COL_LEN):
                possible = 0
                possible = model.NUMBERS.copy()
                if model.grid_m[i][j] != 0:
                    continue
                possible = model.solve_row(model.grid_m, i, possible)
                possible = model.sovle_colmun(model.grid_m, j, possible)
                possible = model.solve_square(model.grid_m, i, j, possible)
                if len(possible) == 1:
                    model.grid_m[i][j] = int(possible[0])
                    continue
                possible = model.neighbour_row(model.grid_m, i, possible)
                possible = model.neighbour_colmun(model.grid_m, j, possible)
                if len(possible) == 1:
                    model.grid_m[i][j] = int(possible[0])
    view.print_grid(model.grid_m) 

if __name__ == '__main__': main()