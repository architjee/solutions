# t = no. of test cases.
t = int(input())
for cases in range(t):
    # n = no. of words written by each person.
    n = int(input())
    s1= input().split()
    s2= input().split()
    s3= input().split()
    bigSet = set()
    bigSet = bigSet.union(s1)
    bigSet = bigSet.union(s2)
    bigSet = bigSet.union(s3)
    bigList = list(bigSet)
    set1 = set(s1)
    set2 = set(s2)
    set3 = set(s3)
    p1, p2, p3= 0,0,0
    for word in bigList:
        if word in s1 and word in s2 and word in s3:
            pass
        elif word in s1 and word in s2:
            p1+=1
            p2+=1
        elif word in s2 and word in s3:
            p2+=1
            p3+=1
        elif word in s1 and word in s3:
            p1+=1
            p3+=1
        elif word in s1:
            p1+=3
        elif word in s2:
            p2+=3
        else:
            p3+=3
    print(p1,p2,p3)             