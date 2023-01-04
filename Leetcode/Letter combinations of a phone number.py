class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'}
        result = []
        def auxillary(idx, partial_ans):
            if idx==len(digits):
                result.append(''.join(partial_ans))
                return 
            for chars in mapping[digits[idx]]:
                auxillary(idx+1, partial_ans+[chars])
        auxillary(0, [])
        return result