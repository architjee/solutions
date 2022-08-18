# We are given an array of size n
# brute force simulation approach.
n, k, q = map(int, input().split())
array = [0] * n
for _ in range(q):
    indexToFlip = int(input()) - 1
    array[indexToFlip] = 1
# We wish to use the concept of Sliding Window.
currentZeros = 0
for i in range(0, k + 1):
    if array[i] == 0:
        currentZeros += 1
low = 0
high = k
ans = k - currentZeros
print("ans at line 16 id :", ans)
while high < n:
    # Now, we will add an element.
    if array[high] == 0:
        currentZeros += 1
    # We must also quickly remove an element from our zero count .
    if array[low] == 0:
        currentZeros -= 1
    low += 1
    high += 1
    ans = min(ans, k - currentZeros)
    print(ans, currentZeros)
