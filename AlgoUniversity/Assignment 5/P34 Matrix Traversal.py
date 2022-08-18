n, m = map(int, input().split())
matrix = [[] for j in range(n)]
for _ in range(n):
    row = list(map(int, input().split()))
    matrix[_] = row
xll = 0
xul = m - 1
yll = 0
yul = n - 1
direction = 0
# We will begin with row = 0 also col = 0
row = 0
col = 0
while xll <= xul and yll <= yul and 0 <= row <= n - 1 and 0 <= col <= m - 1:
    if direction == 0:
        for col in range(xll, xul + 1):
            print(matrix[row][col], end=' ')
        col = xul
        yll += 1
    elif direction == 1:
        for row in range(yll, yul + 1):
            print(matrix[row][col], end=' ')
        row = yul
        xul -= 1
    elif direction == 2:
        for col in range(xul, xll - 1, -1):
            print(matrix[row][col], end=' ')
        col = xll
        yul -= 1
    else:
        for row in range(yul, yll - 1, -1):
            print(matrix[row][col], end=' ')
        row = yll
        xll += 1
    direction = (direction + 1) % 4
