# CodeForces Round 827 Div.4
# A.Sum.py
def main():
    a,b,c = map(int, input().split())
    if(a==(b+c) or b==(a+c) or c==(a+b)):
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range(t):
    main()