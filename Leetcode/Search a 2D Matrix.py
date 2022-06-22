class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # In a question of search in a 2D matrix, we apply the following algorithm:
        # Start with top right
        row = 0
        col = len(matrix[0])-1;
        while( row<len(matrix) and col>=0):
            element = matrix[row][col];
            if(element == target):
                return True;
            elif element < target:
                row +=1
            else:
                col-=1
        return False;