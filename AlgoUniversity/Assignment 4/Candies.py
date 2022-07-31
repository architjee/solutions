n, m = map(int, input().split())
candies = list(map(int, input().split()))
# m is the no. of students and n==len(candies)
assert n == len(candies)
# This is very similar to book allocation problem.
# minimum candies possible is max(candies)

low = max(candies)
high = sum(candies)


def isPossibleToAllocateMaxTheseCandies(maxCandiesAllowed, m):
    studentCounter = 1
    prev = 0
    for candyBox in candies:
        if candyBox > maxCandiesAllowed:
            return False
        elif prev + candyBox > maxCandiesAllowed:
            prev = candyBox
            studentCounter += 1
        else:
            prev += candyBox
    if studentCounter > m:
        return False;
    return True

ans = -1
if n > m:
    while low <= high:
        print(low, high)
        mid = (low + high) // 2
        # Now the maximum no. of candies that can be allocated to one person is mid
        if isPossibleToAllocateMaxTheseCandies(mid, m):
            ans = mid
            # we shall try with a lower number.
            high = mid - 1
        else:
            low = mid + 1

print(ans)
