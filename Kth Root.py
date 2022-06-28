# Partially Solved TestCases for Kth Root Problem
import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(math.floor(math.pow(n, 1/k)))