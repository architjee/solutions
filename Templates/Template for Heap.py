class OurHeap:
    def __init__(self, items):
        self.heap = [None]
        self.rank = {}
        for x in items:
            self.push(items)

    def __len__(self):
        return len(self.heap)-1

    def push(self, item):
        i = len(self.heap)
        self.heap.append(item)
        self.rank[item] = i
        self.up(i)

    def pop(self):
        root = self.heap[1] # Topmost element
        del self.rank[root] # Delete this from the rank
        x = self.heap.pop() # Delete the bottommost element and store it in x
        if self:
            self.heap[1] = x # Moving last leaft to heap
            self.rank[x] = 1;
            self.down(1)
        return root

    def up(self, i):
        x = self.heap[i];
        while i>1 and x < self.heap[i//2]:
            self.heap[i] = self.heap[i//2] # Pull down the element from i//2 to i
            self.rank[self.heap[i]] = i;
            i //=2;
        # We are out of the while loop which must mean that the condition isn't satisfying anymore.
        self.heap[i] = x;
        self.rank[x] = i;

    def down(self, i):
        x = self.heap[i] 
        n = len(self.heap)
        while True:
            left = 2*i
            right = left+1;
            if( right < n and self.heap[right] < x and self.heap[right] < self.heap[left]):
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i
                i= right;
            elif left<n and self.heap[left] < x and self.heap[left]<self.heap[right]:
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i;
                i = left;
            else:
                self.heap[i] = x
                self.rank[x] = i;
                return ;

    def update(self, old , new):
        i= self.rank[old] 
        del self.rank[old]
        self.rank[new] = i;
        if old < new:
            self.down(i)
        else:
            self.up(i)
             

