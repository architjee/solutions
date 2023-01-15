class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_weight_to_curr_row = [0]
        for row in triangle:
            min_weight_to_curr_row = [
                row[j]+min(min_weight_to_curr_row[max(j-1, 0)], min_weight_to_curr_row[min(j, len(min_weight_to_curr_row)-1)]) for j in range(len(row))
            ]
        return min(min_weight_to_curr_row)