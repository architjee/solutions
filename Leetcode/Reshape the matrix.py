class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        result = []
        if(r*c==len(mat)*len(mat[0])):
            for x in mat:
                for y in x:
                    result.append(y)
 
            finalResult = []
            i=0
            for y in range(r):
                temp = []
                for x in range(c): 
                    temp.append(result[i])
                    i+=1;   
                finalResult.append(temp)
            return finalResult
        else:
            return mat