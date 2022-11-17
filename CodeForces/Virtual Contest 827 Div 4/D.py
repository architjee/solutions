import math
# CodeForces Round 827 Div.4
# D.Coprime.py
def main():
    n= int(input())
    arr = list(map(int, input().split()))
    # We will try brute force approach
    def get_max_coprime_indexes(arr):
        ans = -3
        for i in reversed(range(n)):
            for j in reversed(range(i, n)):
                if math.gcd(arr[i], arr[j])==1:
                    ans = max(ans, i+j)
                    return ans+2
                    
        return ans + 2
    
    print(get_max_coprime_indexes(arr))
t = int(input())
for _ in range(t):
    main()