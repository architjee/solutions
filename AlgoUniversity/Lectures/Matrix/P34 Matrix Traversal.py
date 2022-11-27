n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))



def spiral_matrix_traversal(mat):
    pass
    i, j = 0, 0
    hr_size, vr_size = m - 1, n - 1
    
    while hr_size > 0 and vr_size > 0:

        for _ in range(hr_size):
            print(mat[i][j], end=" ")
            j += 1

        for _ in range(vr_size):
            print(mat[i][j], end=" ")
            i += 1
        for _ in range(hr_size):
            print(mat[i][j], end=" ")
            j -= 1
        for _ in range(vr_size):
            print( mat[i][j], end=" ")
            i -= 1
        i+=1
        j+=1
        # reset i and j
        hr_size -=2
        vr_size -=2
    
    print()

spiral_matrix_traversal(matrix)
## The correct answer is supposed to be : 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
## The current output is                  1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 