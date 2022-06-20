class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows ==2:
            return [[1],[1,1]]
        else:
            holdVal = self.generate(numRows-1)
            prevRow = holdVal[-1]
            resultRow = [1]
            for i in range(len(prevRow)-1):
                resultRow.append(prevRow[i]+prevRow[i+1])
            resultRow.append(1)
            holdVal.append(resultRow);
            return holdVal