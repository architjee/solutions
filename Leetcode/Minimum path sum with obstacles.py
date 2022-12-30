class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        def calc_number_of_ways(row_idx, col_idx):
            if row_idx==col_idx==0:
                return int(not obstacleGrid[row_idx][col_idx])
            if obstacleGrid[row_idx][col_idx]==1:
                return 0
            if col_idx<0:
                return 0
            if row_idx<0:
                return 0
            key = (row_idx, col_idx)
            
            if key not in dp:
                dp[key]= calc_number_of_ways(row_idx-1, col_idx) + calc_number_of_ways(row_idx, col_idx-1)
            return dp[key]
        return calc_number_of_ways(len(obstacleGrid)-1,len(obstacleGrid[0])-1)