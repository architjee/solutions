

## Solved fibonacci number:
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        first, second = 0, 1
        third = 0
        for i in range(1,n):
            third = first+second
            first, second = second, third
        return third