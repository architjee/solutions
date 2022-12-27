s = input()
t = input()
import functools
import collections
def hash_of(str):
    return functools.reduce(lambda val, c: val+ord(c) ,str,0)
my_hash = hash_of(s[:len(t)])
hash_of_t = hash_of(t)
counter_t = collections.Counter(t)
my_counter = collections.Counter(s[:len(t)])
known_anagrams = set()
known_anagrams.add(t)
## We will do a rolling hash.
count = 0
for j in range(len(t),len(s)+1):
    ## Check if 
    if my_hash==hash_of_t :
        if s[j-len(t):j] in known_anagrams:
            count += 1
        elif counter_t==my_counter:
            count+=1
            known_anagrams.add(s[j-len(t):j])
    if j<len(s):
        my_hash += ord(s[j])## Adding the hash of the incoming element
        my_counter[s[j]]+=1
    my_counter[s[j-len(t)]]-=1
    if not my_counter[s[j-len(t)]]:
        my_counter.pop(s[j-len(t)])
    my_hash -= ord(s[j-len(t)]) ## Remove the hash of the outgoing element
print(count)