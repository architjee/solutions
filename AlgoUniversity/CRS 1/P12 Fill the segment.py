# We are given an array of size n
# brute force simulation approach.
n, k, q = map(int, input().split())
array = [0] * n
for _ in range(q):
    indexToFlip = int(input()) - 1
    array[indexToFlip] = 1
# We wish to use the concept of Sliding Window.
currentOnes = 0
for i in range(0, k):
    if array[i] == 1:
        currentOnes += 1
low = 0
high = k
ans = currentOnes

while high < n:
    # Now, we will add an element.
    if array[high] == 1:
        currentOnes += 1
    # We must also quickly remove an element from our one count .
    if array[low] == 1:
        currentOnes -= 1
    low += 1
    high += 1
    ans = min(ans, currentOnes)
print(ans)
