s = input()
t = input()
result = (-1, -1)
import collections
keywords_to_search = collections.Counter(t)
left = 0
remaining = len(t)
for right, c in enumerate(s):
    if c in keywords_to_search:
        keywords_to_search[c]-=1
        if keywords_to_search[c]>=0:
            remaining-=1
    while remaining == 0:
        if result == (-1,-1 ) or right-left<result[1]-result[0]:
            result = (left, right)
        left_ele = s[left]
        if left_ele in keywords_to_search:
            keywords_to_search[left_ele]+=1
            if keywords_to_search[left_ele]>0:
                remaining+=1
        left += 1
if result == (-1,-1):
    print(-1)
else:
    print(result[1]-result[0]+1)
