n, m ,Q = map(int, input().split())
bigList = []
firstCol = []
for i in range(n):
    bigList.append(list(map(int, input().split())))
    firstCol.append(bigList[-1][0])
import bisect
queries = map(int, input().split())
for query in queries:
    row_idx = bisect.bisect_left(firstCol, query)   
    if row_idx==-1:
        row_idx=0
    print(row_idx, bisect.bisect_left(bigList[row_idx], query))
    