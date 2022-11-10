try:
    s1, s2 = input().lower().split(' ')
    import collections
    s1Dic=collections.Counter(s1)
    s2Dic= collections.Counter(s2)
    import string
    result = True
    import math
    for c in string.ascii_lowercase:
        if c in s1Dic and c not in s2Dic:
            if(s1Dic[c]>3):
                result = False
                break
        if c in s2Dic and c not in s1Dic:
            if s2Dic[c]>3:
                result = False
                break
        if c in s1Dic and c in s2Dic:
            if math.fabs(s1Dic[c]-s2Dic[c])>3:
                result = False;
                break
    if result:
        print("YES")
    else:
        print("NO")
except:
    print("NO")