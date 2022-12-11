
from sys import *
from collections import *
from math import *
def uniquePaths(m, n):
    # Write your code here.
    ways_matrix = [[0]*(m+1) for _ in range(n+1)]
    def unique_paths_util(col, row):
        if col==0 and row == 0:
            return 1
        if ways_matrix[row][col]==0:
            ways_colwards = 0 if col==0 else unique_paths_util(col-1, row)
            ways_rowwards = 0 if row==0 else unique_paths_util(col, row-1)
            ways_matrix[row][col] = ways_colwards + ways_rowwards
        return ways_matrix[row][col]
    return unique_paths_util(m-1, n-1)
        