from typing import *

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ## Thing to note here, there are not asking us to preserve the integrity of any good line, but simply put just checking if it is a good line's enedpoint would suffice.
        DIRECTIONS_ARR = [[0,1],[1,0],[0,-1],[-1,0],
                # Diagonal counter-clockwise.
                [-1,1],[-1,-1],[1,-1],[1,1]
        ]
        
        def next_coordinate(direction, coordinate):
            if direction==0:
                return coordinate
            elif direction==1:
                return coordinate+1
            elif direction==-1:
                return coordinate-1
            return coordinate
        for direction in DIRECTIONS_ARR:
            direction_x, direction_y = direction
            next_x = next_coordinate(direction_x, cMove)
            next_y = next_coordinate(direction_y, rMove)
            while 0<=next_x<len(board[0]) and 0<=next_y<len(board) and board[next_y][next_x]!='.' and board[next_y][next_x]!=color:
                # So this coordinate was good we will add this to our run and move on. 
                next_x = next_coordinate(direction_x, next_x)
                next_y = next_coordinate(direction_y, next_y)
            if 0<=next_x<len(board[0]) and 0<=next_y<len(board) and board[next_y][next_x]==color:
                return True
        return False

                