def distinctAverages(nums):
        avgSet = set()
        while nums:
            mine = min(nums)
            maxe = max(nums)
            avg = (mine+maxe)/2
            avgSet.add(avg)
            nums.remove(mine)
            nums.remove(maxe)
        return len(avgSet)
print(distinctAverages([4,1,4,0,3,5]))