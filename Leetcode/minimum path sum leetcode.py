class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        d = {}
        def aux_path_sum(row_idx, col_idx):
            if row_idx==0 and col_idx==0:
                return grid[row_idx][col_idx]
            key = row_idx, col_idx
            if key not in d:
                left_val = float('inf')
                right_val = float('inf')
                if col_idx>0:
                    left_val = aux_path_sum(row_idx,col_idx-1)
                if row_idx>0:
                    right_val = aux_path_sum(row_idx-1, col_idx)
                d[key] = grid[row_idx][col_idx]+ min(left_val,right_val)
            return d[key]
        return aux_path_sum(len(grid)-1, len(grid[0])-1)    