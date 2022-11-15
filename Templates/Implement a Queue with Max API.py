
import collections
class QueueWithMax:
    def __init__(self):
        self.elements = collections.deque()
        self._cam = collections.deque()

    def enqueue(self, x):
        self.elements.append(x)
        while self._cam and self._cam[-1]<x:
            self._cam.pop()
        self._cam.append(x)

    def dequeue(self):
        if self.elements:
            result = self.elements.popleft()
            if result==self._cam[0]:
                self._cam.popleft()
            return result
        raise IndexError
    def max(self):
        if self._cam:
            return self._cam[0]
        raise IndexError