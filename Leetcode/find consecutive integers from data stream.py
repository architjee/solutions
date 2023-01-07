import collections
class DataStream:

    def __init__(self, value: int, k: int):
        self.q = collections.deque([value])
        self.d = collections.defaultdict()
        self.d[value]=1
        self.k = k

    def consec(self, num: int) -> bool:
        self.q.append(num)
        self.d[num]+=1
        if len(self.q)>self.k:
            outgoing=self.q.popleft()
            if outgoing in self.d:
                self.d[outgoing]-=1
            if self.d[outgoing]==0:
                del self.d[outgoing]
        if len(self.q)==self.k and len(self.d)==1:
            return True
        return False


## WARNING WRONG FILE DELETE THIS
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)