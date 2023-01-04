class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        result = []
        prev_answer = self.countAndSay(n-1)
        index = 0
        while index < len(prev_answer):
            start = index
            count = 1
            while start<len(prev_answer)-1 and prev_answer[start+1]==prev_answer[start]:
                start+=1
                count +=1
            result.append(str(count))
            result.append(prev_answer[index])
            index = start + 1
        return ''.join(result)