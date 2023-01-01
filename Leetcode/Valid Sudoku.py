class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = True
    
        for x in range(9):
            result = result and self.validateRow(x, board)
            result = result and self.validateColumn(x, board)
            # print("Validating Row and Column as ",x )
        result = result and self.validateCoordinates(
            0, 0, 3,3 , board) and self.validateCoordinates(
            0, 3, 3,6 , board) and self.validateCoordinates(
            0, 6, 3,9 , board) and self.validateCoordinates(
            3, 0, 6,3 , board) and self.validateCoordinates(
            3, 3, 6,6 , board) and self.validateCoordinates(
            3, 6, 6,9 , board) and self.validateCoordinates(
           6, 0, 9,3 , board) and self.validateCoordinates(
           6, 3, 9,6 , board) and self.validateCoordinates(
           6, 6, 9,9 , board)
        return result
        ## random comment
    def validateRow(self,row, board):
        return self.validateCoordinates( row, 0, row+1, 9, board)
        
    
    def validateColumn(self,column, board):
        return self.validateCoordinates( 0, column, 9, column+1, board)
    
    def validateCoordinates(self, top, left, bottom, right, board):
        # print("Top:",top,"Left:",left,"Bottom:",bottom,"Right:",right)
        row = top
        d = set()
        while row<bottom:
            column = left
            while column<right:
                if(board[row][column]!="."):
                    key = int(board[row][column])
                    # print("Executing for key",key,"row",row,"column",column)
                    if key in d:
                        print("Hey this resturn value is false;")
                        return False;
                    d.add(key)
                column+=1
            row+=1
        return True