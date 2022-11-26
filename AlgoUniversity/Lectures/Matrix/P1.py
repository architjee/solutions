# Solved successfully problem P1 in python.

def print_matrix_in_snake_pattern(mat):
    for index, row in enumerate(mat):
        if index%2==0:
            for ele in row:
                print(ele, end=' ')
        else:
            for ele in reversed(row):
                print(ele, end=' ')

print_matrix_in_snake_pattern([[1,2,3],[4,5,6],[7,8,9],])