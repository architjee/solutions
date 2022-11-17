# CodeForces Round 827 Div.4
# A.Increasing.py
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    if len(set(arr))==n:
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range(t):
    main()