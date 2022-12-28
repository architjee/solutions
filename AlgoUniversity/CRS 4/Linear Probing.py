class CustomHash:
    def __init__(self, m):
        self.d = {}
        self.array = [-1 for x in range(m)]
    def set(self, x):
        if x in self.d:
            return self.d[x]
        idx = x
        if len(self.d)>=m:
            return
        while self.array[idx%m]!=-1:
            idx += 1
        self.array[idx%m]= x
        self.d[x] = idx
    def printArray(self):
        print(*self.array, sep=' ')
n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = [-1 for x in range(m)]
hash_table = CustomHash(m)
for x in arr:
    hash_table.set(x)
hash_table.printArray()
