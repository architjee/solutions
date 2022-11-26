## Boundary Traversal problem (---> then last column top to down, last row right to left, and first column bottom to top).
## Printing while j==0 j==n-1 i==0 and i==n-1, for all others 

def print_boundary_traversal_of_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(0, n):
        for j in range(0, m):
            if i==0 or j==0 or i==n-1 or j==m-1:
                print(mat[i][j], end=' ')
            else:
                print(' ', end=' ')
        print()

mat = [[1 ,2, 3, 4],
[5, 6, 7, 8,],
[9, 10, 11, 12],
[13 ,14 ,15 ,16]]
print_boundary_traversal_of_matrix(mat)
