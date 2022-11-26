## Method 1 to solve the problem by using some extra memory.

def m1(mat):
    n = len(mat)
    m = len(mat[0])
    transpose_matrix = [[0 for i in range(n)] for j in range(m)]
    for i in range(0, n):
        for j in range(0, m):
            transpose_matrix[j][i]=mat[i][j]
    return transpose_matrix
mat = [[1 ,2, 3, 4],
[5, 6, 7, 8,],
[9, 10, 11, 12],
[13 ,14 ,15 ,16]]

print(m1(mat))
## But method 1 uses extra memory can we do it without extra space???

## Method 2 , Trying to do it in-place.

def m2(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(0, n):
        for j in range(i+1, m):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat
print(m2(mat))

# Both methods test cases passed. Good job.