class LRUCache:

    def __init__(self, capacity: int):
        self.table = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        value = self.table.pop(key)
        self.table[key]=value
        return value 

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table.pop(key)
        self.table[key] = value
        if len(self.table)>self.capacity:
            self.table.popitem(last=False)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)