n = int(input())


def findSquareBetween(suspect, target):
    low = suspect - 1
    high = suspect
    while True:
        root = (low + high) / 2.0
        currentSquare = root*root
        if currentSquare == target or abs(currentSquare - target) < 0.000000001:
            return root
        elif root * root > target:
            high = root
        else:
            low = root

# Let us say that n is a Perfect Square, Now can we solve this problem.
for i in range(0, n):
    if i * i == n:
        print(i)
        break
    elif i * i > n:
        # Well in that case. Find the sqrt between n-1 and n
        ans = findSquareBetween(i, n)
        print(ans)
        break