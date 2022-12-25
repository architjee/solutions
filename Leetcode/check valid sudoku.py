class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def eval_data(data):
            c = collections.Counter(data)
            for key, value in c.items():
                if key=='.':
                    continue
                if value > 1:
                    return False
            return True
        def check_row(row_idx):
            row = board[row_idx]
            return eval_data(row)
            
        for i in range(len(board)):
            if not check_row(i):
                return False
        
        def check_col(col_idx):
            col_data = [board[x][col_idx] for x in range(len(board))]
            return eval_data(col_data)
        for j in range(len(board[0])):
            if not check_col(j):
                return False
        def check_sub_grid(row_idx, col_idx):
            grid_data = [board[row_idx+y][col_idx+x] for x in range(3) for y in range(3)]
            return eval_data(grid_data)
        for y in range(0, len(board), 3):
            for x in range(0, len(board[0]), 3):
                if not check_sub_grid(y, x):
                    return False    
        return True
        