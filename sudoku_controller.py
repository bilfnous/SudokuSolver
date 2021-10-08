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
    model.read_grid(model.grid_m)
    view.print_grid(model.grid_m)
   # possible = model.solve_row(model.grid_m, 0, possible)
   # possible = model.sovle_colmun(model.grid_m, 0, possible)
   # possible = model.solve_square(model.grid_m, 0, 0, possible)
    print (possible)

if __name__ == '__main__': main()