# Program to print Permutations of a String. 

s = input()

# s is the given string
# also given in constraints that length of s <=8

listOfChars = list(s)
result = []

# Utility function to convert permutation to string.
def convertPermToString(listOfChars):
    return ''.join(listOfChars)

def getAllPermutations(listOfChars, i):

    # We will consider that we have already printed the s for i-1 characters,
    # We are concerned with printing ith character and only the [i:] part of the list.
    if i==len(listOfChars)-1:
        result.append(convertPermToString(listOfChars))
        return
    for j in range(i, len(listOfChars)):
        # Swapping i and j
        listOfChars[i], listOfChars[j] = listOfChars[j], listOfChars[i]
        getAllPermutations(listOfChars, i+1)

        # Back Tracking
        listOfChars[j], listOfChars[i] = listOfChars[i], listOfChars[j] 

getAllPermutations(listOfChars, 0)
result.sort()
for combination in result:
    print(combination)