#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __auther__ B. Alfanous
# __email__ b.alfanous@outlook.com
# __date__ 28/Mar/2020
# __file__ sudoku_model.py


grid_m = [[0 for i in range(9)] for i in range(9)]

def print_grid(grid_m):
    print("- - - - - - - - - - - - - - - - -")
    for i in range(len(grid_m)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - -")

        for j in range(len(grid_m[0])):
            if j % 3 == 0 and j != 0:
                print(" |  ", end="")

            if j == 8:
                print(str(grid_m[i][j]) + " ")
            else:
                print(str(grid_m[i][j]) + "  ", end="")
    
    print("- - - - - - - - - - - - - - - - -")
    
def main():
    print_grid(grid_m)
    print("Fill in the sudoku grid; enter 0 to fill the empty square: ")
    for i in range(9):
        for j in range(9):
            grid_m[i][j] = input(f'[{i + 1}] [{j + 1}] >> ')
            

if __name__ == '__main__': main()