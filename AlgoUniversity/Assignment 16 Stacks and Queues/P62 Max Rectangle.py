# Answer for the following test case is 10
# 6
# 2 1 5 6 2 3
import collections
n = int(input())
arr = list(map(int, input().split()))
def createNearestSmallestLeft(arr):
    idx_height = collections.namedtuple('idx_height',('idx', 'height'))
    result = []
    stk = []
    for index, x in enumerate(arr):
        if not stk:
            stk.append(idx_height(index, x))
            result.append(-1)
        else:
            while stk and stk[-1].height>x:
                stk.pop()
            if not stk:
                result.append(-1)
            else:
                result.append(stk[-1].idx)
            stk.append(idx_height(index, x))
    return result
print(createNearestSmallestLeft(arr))
