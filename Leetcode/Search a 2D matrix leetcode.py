class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col_data = [matrix[i][0] for i in range(len(matrix))]
        import bisect
        row_idx = bisect.bisect_left(first_col_data, target)
        if row_idx>len(matrix)-1:
            row_idx = -1
        if matrix[row_idx][0]==target:
            return True
        if row_idx > 0:
            row_idx-=1
        col_idx = bisect.bisect_left(matrix[row_idx], target)
        if col_idx>len(matrix[0])-1:
            return False
        if matrix[row_idx][col_idx]==target:
            return True
        return False