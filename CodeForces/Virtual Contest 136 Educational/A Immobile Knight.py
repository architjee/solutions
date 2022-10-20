def mainFunc():
    # Given two numbers
    n , m = map(int,input().split())
    # We have a n rows and m columns
    if n<=3 or m<=3:

        if n%2:
            n=(n//2)+1
        else:
            n=n//2
        if m%2:
            m=(m//2)+1
        else:
            m=m//2
    print(n,m)
t = int(input())

for testcases in range(t):
    mainFunc()