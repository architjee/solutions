class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def directed_generate(num_left_needed, num_right_needed, valid_prefix):
            if num_left_needed>0:
                directed_generate(num_left_needed-1, num_right_needed, valid_prefix+'(')
            if num_left_needed<num_right_needed:
                directed_generate(num_left_needed, num_right_needed-1, valid_prefix+')')
            if not num_right_needed:
                result.append(valid_prefix)
            return result
        return directed_generate(n, n,'')