n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def checkThisDiag(matrix, starti, startj, n, m):
    flag = True
    prevElement = matrix[starti][startj]
    starti+=1
    startj+=1
    while starti<n and startj<m:
        currentElement = matrix[starti][startj]
        if currentElement == prevElement:
            pass
        else:
            flag = False
            break
        starti+=1
        startj+=1
    return flag
# This question is very easy once you see the pattern.

# We must move from Top Right to Top Left and then From Top Left to Bottom Left
#   i.e.    <-----------------
# and then  |
#           |
#           |
#           V

# We will iterate from top right to top left.
i=0
flag = True
for j in range(m-1, -1, -1):
    if not(checkThisDiag(matrix, i, j, n, m)):
        flag = False
        break
j=0
for i in range(1, n):
    if not (checkThisDiag(matrix, i, j, n, m)):
        flag = False
        break
if flag:
    print(1)
else:
    print(0)