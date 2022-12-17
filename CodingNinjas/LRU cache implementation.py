
from sys import stdin
import collections
class LRUCache:
	# Initialize the LRU Cache
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = collections.OrderedDict()
        
    def get(self, key):
        # Your code goes here
        if key in self.hashtable:
            value = self.hashtable.pop(key)
            self.hashtable[key] = value
            return value
        return -1
	
    def put(self, key, value):
        # Your code goes here
        
        if key in self.hashtable:
            ## Key exist in the hashtable so we will pop it out and push it again.
            existing_value = self.hashtable.pop(key)
        if len(self.hashtable)>=self.capacity:
            self.hashtable.popitem(last=False)
        self.hashtable[key] = value

# main
capacity, q = map(int, stdin.readline().rstrip().split(" "))

cache = LRUCache(capacity)

while q != 0:
	query = list(map(int, stdin.readline().rstrip().split()))

	if query[0] == 0:
		key = query[1]
		print(cache.get(key))
	elif query[0] == 1:
		key = query[1]
		value = query[2]
		cache.put(key, value)
	
	q -= 1