from itertools import permutations


thesarus = {}
result = []
for x in range(1,51):
    result.append(x)
    thesarus[x] = result[0:]
# print(thesarus)
def mainFunc():
    # Given n <=50
    n = int(input())

    # A function to just check whether the given subarray is a permutation or not.
    def checkPerm(perm):
        # print("checkPerm is being called for ", perm)
        if thesarus[len(perm)]==sorted(list(set(perm))):
            # print("return True for this guy")
            return True
        return False
    # I am thinking some brute force sort of approach.
    def evaluatePermutaion(perm):
        counte = 0
        if checkPerm(perm):
            # We will check each permutation for both start and end index motion 
            counte+=1
            for start in range(0, len(perm)-1):
                for stop in range(start+1, len(perm)):
                    if checkPerm(perm[start:stop]):
                        # print("Getting true for start", start, "and stop at", stop, perm[start:stop], " and count is now", count)
                        counte += 1
        return counte
    result = thesarus[n]
    result = result[1:]+[result[0]]
    
    
    for ele in result:
        print(ele, end=' ')
    print()

t = int(input())
for testcase in range(t):
    mainFunc()