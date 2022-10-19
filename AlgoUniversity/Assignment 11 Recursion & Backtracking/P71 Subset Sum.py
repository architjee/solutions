n = int(input())
nums = list(map(int, input().split()))
# The total number of nos allowed in the array are 20.
totalSum = sum(nums)

powerSet = [];
def generateSums(nums, i, currentSum):
    if i==len(nums):
        powerSet.append(currentSum)
        return

    # We can choose to either include it 
    currentSum += nums[i]
    generateSums(nums, i+1, currentSum)

    # Or we can choose to exclude it
    
    currentSum -= nums[i]
    generateSums(nums, i+1, currentSum )
minDiff = float('inf')
generateSums(nums, 0, 0)
for sum1 in powerSet: 
    diffStore = abs(totalSum-2*sum1)
    minDiff = min(diffStore,minDiff )
print(minDiff)