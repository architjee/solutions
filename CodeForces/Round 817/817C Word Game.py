# t is no. of test cases.
t= int(input())
for _ in range(t):
    n = input()
    d = {}
    s1 = input().split()
    s2= input().split()
    s3 =input().split()
    p1,p2,p3 = 0,0,0
    for word in s1:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    for word in s2:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    for word in s3:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    for word in s1:
        if d[word]==3:
            pass
        elif d[word]==2:
            p1+=1
        else:
            p1+=3
    for word in s2:
        if d[word]==3:
            pass
        elif d[word]==2:
            p2+=1
        else:
            p2+=3
    for word in s3:
        if d[word]==3:
            pass
        elif d[word]==2:
            p3+=1
        else:
            p3+=3
    print(p1,p2,p3)