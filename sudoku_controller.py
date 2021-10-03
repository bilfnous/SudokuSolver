#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__file__ = "sudoku_controller.py"
__auther__ = "B. Alfanous"
__email__ = "b.alfanous@outlook.com"
__date__ = "28/Mar/2020"


import sudoku_model as model
import sudoku_view as view


def main():
    view.print_grid(model.grid_m)
    model.read_grid(model.grid_m)
    view.print_grid(model.grid_m)
            
if __name__ == '__main__': main()