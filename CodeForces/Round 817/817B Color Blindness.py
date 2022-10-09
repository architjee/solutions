# t is the no. of test cases.
t = int(input())
for x in range(t):
    n = int(input())
    s1 = list(input())
    s2 = list(input())
    for index, value in enumerate(s1):
        if s1[index]=="G":
            s1[index]="B"
        if s2[index]=="G":
            s2[index]="B"
    if s1==s2:
        print("YES")
    else:
        print("NO")
