#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __auther__ B. Alfanous
# __email__ b.alfanous@outlook.com
# __date__ 28/Mar/2020
# __file__ sudoku_model.py


    
    
def main():
    grid_m = [[0 for i in range(9)] for i in range(9)]
    print("Fill in the sudoku grid; enter 0 to fill the empty square: ")
    for i in range(9):
        for j in range(9):
            grid_m[i][j] = input(f'[{i + 1}] [{j + 1}] >> ')

if __name__ == '__main__': main()
