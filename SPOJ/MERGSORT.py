# The problem statement is  Simple.
# Sort the numbers on the standard input using the merge sort algorithm.
# Don't try to cheat by just calling your build in functions.
def mergeTwoSmall(x, y):
    z = []
    i = 0
    j = 0
    while i < len(x) or j < len(y):
        if j == len(y) or i < len(x) and x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    return z


def mergeSort(array):
    if (len(array) == 1):
        return array
    if array:
        # Then only we would like to perform some computation.
        x = mergeSort(array[:len(array) // 2])
        y = mergeSort(array[len(array) // 2:])
        array = mergeTwoSmall(x, y)
        return array
    return array


def printArrayFunc(array):
    for x in array:
        print(x, end=' ')


def main():
    array = list(map(int, input().split()))
    array = mergeSort(array)
    printArrayFunc(array)


main()
