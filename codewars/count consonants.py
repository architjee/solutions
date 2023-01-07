import collections
import string
def consonant_count(s):
    s = s.lower()
    mycounter = collections.Counter(s)
    ans = 0
    for consonant in string.ascii_lowercase :
        if consonant not in "aeiou":
            ans += mycounter[consonant]
    return ans