from os import *
from sys import *
from collections import *
from math import *

def searchMaze(arr, n):
    # Write your code here.
    x, y =0, 0
    BLOCKED, OPEN = 0, 1
    d = [[0,1,'D'],[1,0,'R'],[0,-1,'U'],[-1,0,'L']]
    def validate_coordinate(x ,y):
        if x>=0 and x<n and y>=0 and y<n:
            return True
        return False
    result = []
    def dfs_helper(x,y, partial_path):
        if x==n-1 and y==n-1:
            result.append(''.join(reversed(partial_path)))
            ## This block is open for traversing, so we will block it ourselves before moving on.
        arr[x][y]=BLOCKED
        for dir_x, dir_y, move in d:
            new_x, new_y = x+dir_x, y+dir_y
            if validate_coordinate(new_x, new_y) and arr[new_x][new_y]==OPEN:
                partial_path.append(move)
                dfs_helper(new_x, new_y, partial_path)
                partial_path.pop()
        arr[x][y]=OPEN
    if arr[0][0]==OPEN:
        dfs_helper(0, 0,[])
    # print('result looks like this', result)
    result.sort()
    return result