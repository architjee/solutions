class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp_array = [[[]]+[[]]*target for x in candidates]
        for i in range(len(candidates)):
            for j in range(1, target+1):
                ## We have to target B inclusive
                without_this_element = []
                if i>=1:
                    without_this_element = dp_array[i-1][j]
                with_this_element = []
                if j>candidates[i]:
                    for combination in dp_array[i][j-candidates[i]]:
                        with_this_element.append(combination+[candidates[i]])
                elif j==candidates[i]:
                    with_this_element = [[candidates[i]]]
                dp_array[i][j] = without_this_element + with_this_element
        ans = dp_array[-1][-1]
        for seq in ans:
                seq.sort()
        return ans
            