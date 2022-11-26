mat = [[1 ,2, 3, 4],
[2, 5, 6, 8,],
[3, 10, 15, 18],
[4 ,12 ,20 ,40]]

## Given each element is unique.
## You need to implement search in a row-wise and column-wise sorted matrix. Search for a given element k.
def search_in_rowwise_columnwise_sorted(mat, k):
    pass

## There are manhy solutions possible.
# O(n2) or better O(nlogM) or better O(n+m) or better Log(n+m)

## For n2 is very simple. You need to search an element k in the matrix.
## Just traverse the full matrix.

## we can do binary search in every row. That is cost 
## us n log m
# if my k is greater than a[i][j]

# O(N+M) if we start from top right we can go either left or we can go down.

## Take a 2d array 1 2 3 4 
##                  5 6  7 8 
##                  9 10 11 12
##                  13 14 15 16

## Now try to think of Log(n)+ logm) solution.

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20

# upper bound -1 vaali row mein hi hoga answer
# log N + log M
# This will be 4th question of this assignment.
