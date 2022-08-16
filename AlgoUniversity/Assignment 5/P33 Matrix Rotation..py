n = int(input())
matrix = []
def transposeOfMatrix(matrix, size):
    for i in range(0, size):
        for j in range(i+1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
def reverseAllColumns(matrix, size):
    for col in range(0, size):
        low = 0
        high = size - 1
        while low<high:
            matrix[low][col], matrix[high][col] = matrix[high][col] , matrix[low][col]
            low+=1
            high -=1
def printMatrixSpacedOut(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
for _ in range(n):
    row = []
    row = list(map(int, input().split()))
    matrix.append(row)
transposeOfMatrix(matrix, n)
reverseAllColumns(matrix, n)
printMatrixSpacedOut(matrix)
