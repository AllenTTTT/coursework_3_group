#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:08:15 2023

@author: a
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 23:01:52 2023

@author: a
"""
import time
import numpy as np
import sys
sys.setrecursionlimit(100000)
easy_1 = [[9, 0, 6, 0, 0, 1, 0, 4, 0],
[7, 0, 1, 2, 9, 0, 0, 6, 0],
[4, 0, 2, 8, 0, 6, 3, 0, 0],
[0, 0, 0, 0, 2, 0, 9, 8, 0],
[6, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 9, 4, 0, 8, 0, 0, 0, 0],
[0, 0, 3, 7, 0, 8, 4, 0, 9],
[0, 4, 0, 0, 1, 3, 7, 0, 6],
[0, 6, 0, 9, 0, 0, 1, 0, 8]]
easy_2 = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
[6, 8, 0, 0, 7, 0, 0, 9, 0],
[1, 9, 0, 0, 0, 4, 5, 0, 0],
[8, 2, 0, 1, 0, 0, 0, 4, 0],
[0, 0, 4, 6, 0, 2, 9, 0, 0],
[0, 5, 0, 0, 0, 3, 0, 2, 8],
[0, 0, 9, 3, 0, 0, 0, 7, 4],
[0, 4, 0, 0, 5, 0, 0, 3, 6],
[7, 0, 3, 0, 1, 8, 0, 0, 0]]
easy_3 = [[0, 3, 0, 4, 0, 0],
[0, 0, 5, 6, 0, 3],
[0, 0, 0, 1, 0, 0],
[0, 1, 0, 3, 0, 5],
[0, 6, 4, 0, 3, 1],
[0, 0, 1, 0, 4, 6]]
med_1 = [[0, 0, 0, 6, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 5, 0, 1],
[3, 6, 9, 0, 8, 0, 4, 0, 0],
[0, 0, 0, 0, 0, 6, 8, 0, 0],
[0, 0, 0, 1, 3, 0, 0, 0, 9],
[4, 0, 5, 0, 0, 9, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 0, 0],
[0, 0, 6, 0, 0, 7, 0, 0, 0],
[1, 0, 0, 3, 4, 0, 0, 0, 0]]
med_2 = [[8, 0, 9, 0, 2, 0, 3, 0, 0],
[0, 3, 7, 0, 6, 0, 5, 0, 0],
[0, 0, 0, 4, 0, 9, 7, 0, 0],
[0, 0, 2, 9, 0, 1, 0, 6, 0],
[1, 0, 0, 3, 0, 6, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 3],
[7, 0, 0, 0, 0, 0, 0, 0, 8],
[5, 0, 0, 0, 0, 0, 0, 1, 4],
[0, 0, 0, 2, 8, 4, 6, 0, 5]]
hard_1 = [[0, 2, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 6, 0, 4, 0, 0, 0, 0],
[5, 8, 0, 0, 9, 0, 0, 0, 3],
[0, 0, 0, 0, 0, 3, 0, 0, 4],
[4, 1, 0, 0, 8, 0, 6, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 9, 5],
[2, 0, 0, 0, 1, 0, 0, 8, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 3, 1, 0, 0, 8, 0, 5, 7]]
easy_1_r = np.loadtxt("../easy1.txt", dtype=int, delimiter=',')
easy_2_r = np.loadtxt("../easy2.txt", dtype=int, delimiter=',')
easy_3_r = np.loadtxt("../easy3", dtype=int, delimiter=',')
med_1_r = np.loadtxt("../med1", dtype=int, delimiter=',')
med_2_r = np.loadtxt("../med2", dtype=int, delimiter=',')
hard_1_r = np.loadtxt("..hard1", dtype=int, delimiter=',')
grids_r = [(easy_1_r,3,3) ,(easy_2_r, 3, 3), (easy_3_r, 2, 3), (med_1_r, 3, 3), (med_2_r, 3, 3), (hard_1_r, 3, 3)]
grids = [(easy_1,3,3) ,(easy_2, 3, 3), (easy_3, 2, 3), (med_1, 3, 3), (med_2, 3, 3), (hard_1, 3, 3)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def check_section(section,n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
        return True
    return False

def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved

    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows*n_cols

    for row in grid:
        if check_section(row, n) == False:
            return False

    for i in range(n_rows**2):
        column = []
        for row in grid:
            column.append(row[i])

        if check_section(column, n) == False:
            return False
#    squares = get_squares(grid, n_rows, n_cols)
    for square in grid:
        if check_section(square, n) == False:
            return False

    return True
def find_empty(grid):
    '''
    This function returns the index (i, j) to the first zero element in a sudoku grid
    If no such element is found, it returns None

    args: grid
    return: A tuple (i,j) where i and j are both integers, or None
    '''

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                return (i, j)

    return None

def value(grid,n_rows,n_cols):
    x,y =find_empty(grid)
    i,j = x//n_rows,y//n_cols
    grid_m = [grid[i*n_rows+r][j*n_cols+c] for r in range(n_rows) for c in range(n_cols)]
    v = set([x for x in range(1,n_rows*n_cols+1)]) - set(grid_m) - set(grid[x]) - \
        set(list(zip(*grid))[y])    
    return list(v)

def recursive_solve(grid, n_rows, n_cols, prev_moves=[]):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''

    #Find an empty place in the grid
    empty = find_empty(grid)


    #If there's no empty places left, check if we've found a solution
    if not empty:
        #If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid, prev_moves
        else:
            #If the solution is incorrect, return None
            return None
    else:
        row, col = empty 

    #Loop through possible values
    for i in value(grid,n_rows,n_cols):
            #Place the value into the grid
            prev_moves.append((row,col,i))
            grid[row][col] = i
            #Recursively solve the grid
            ans = recursive_solve(grid, n_rows, n_cols, prev_moves)
            #If we've found a solution, return it
            if ans:
                return ans

            #If we couldn't find a solution, that must mean this value is incorrect.
            #Reset the grid for the next iteration of the loop
            grid[row][col] = 0
            prev_moves.pop()

    #If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None

def explain_moves(moves):
    for row,col,i in moves:
        f = open("output.txt",'a+')
        f.write(f'Put {i} in {row},{col}'+'\n')
#        print(f'Put {i} in {row},{col}')

def solve(grid, n_rows, n_cols):

    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''
    
    sol, moves = recursive_solve(grid, n_rows, n_cols)
    explain_moves(moves)
    with open('output.txt','a+') as f: 
        f.write('========================'+'\n')
    with open('output.txt','ab') as f:
        np.savetxt(f,sol,fmt = '%i',delimiter=',')
    with open('output.txt','a+') as f: 
        f.write('========================'+'\n')
#            for (i, (grid, n_rows, n_cols)) in enumerate(grids):
    return sol

'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():

    points = 0

    print("Running test script for coursework 3")
    print("====================================")
    
    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i+1))
        start_time = time.time()
        solution = solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(np.array(solution))
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i+1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i+1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)



if __name__ == "__main__":
    main()