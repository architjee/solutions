def transpose_matrix(mat,n):
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j], mat[j][i]= mat[j][i], mat[i][j]
def rotate_matrix_90_anti(mat, n):
    transpose_matrix(mat, n)
n = int(input())
mat = []
for rows in range(n):
    mat.append(list(map(int, input().split())))
for index,row in enumerate(mat):
    row.reverse()
rotate_matrix_90_anti(mat, n)
for row in mat:
    print(*row, end=' ')