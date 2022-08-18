n, m, q = map(int, input().split())
matrix = [[] for i in range(n)]


def searchAndPrintIndices(matrix, target):
    # Find upper bound in the first indices of the matrix.
    # Once we have finalized
    low = 0
    high = n - 1
    while low + 1 < high:
        midix = (low + high) // 2
        midElement = matrix[midix][0]
        if midElement <= target:
            low = midix
        else:
            high = midix
    # As of now we will only print the target.
    return low


def binarySearch(row, target):
    low = 0
    high = len(row) - 1

    while low + 1 < high:
        mid = (low + high) // 2
        if (row[mid] - target) <= 0:
            low = mid
        else:
            high = mid
        return low


for i in range(n):
    matrix[i] = list(map(int, input().split()))
queries = list(map(int, input().split()))
for target in queries:
    rowIndex = searchAndPrintIndices(matrix, target)
    print(target, rowIndex)
    print(binarySearch(matrix[rowIndex], target))
    