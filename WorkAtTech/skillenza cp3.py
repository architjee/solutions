s = input()
import collections
import string
c = collections.Counter(s)
for x in s:
    if c[x]==1:
        print(s.index(x))
        break