n = int(input())
import math
def compute_square_root_of_n(n):
    left, right = (0, 1.0) if n<1.0 else (1.0, n)
    while not math.isclose(left, right):
        mid = (left+right)/2
        mid_squared = mid*mid
        if mid_squared>n:
            right = mid
        else:
            left = mid
    return left
print(compute_square_root_of_n(n))