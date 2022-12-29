n= int(input())
arr = [x for x in range(1, n+1)]
permutations = []
def createPermutations(nums, i):
    if i==len(nums)-1:
        permutations.append(nums[0:])
        return 
    for x in range(i, len(nums)):
        nums[i], nums[x] = nums[x], nums[i]
        createPermutations(nums, i+1)
        nums[i], nums[x] = nums[x], nums[i]
createPermutations(arr, 0)
print(permutations)
for permutation in permutations:
    if 