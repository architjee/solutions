# t is no. of test cases
t = int(input())
for x in range(t):
    n = int(input())
    s = input()
    if n==5 and sorted(s)==sorted("Timur"):
        print("YES")
    else:
        print("NO")