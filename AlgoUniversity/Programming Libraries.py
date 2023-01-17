import collections
n, m = map(int, input().split())
indegree = [0 for x in range(n)]
adj_list = collections.defaultdict(list)
for ti in range(m):
    u, v = map(int, input().split())
    indegree[v]+=1
    adj_list[u].append(v)
node_with_in_zero = [index for index, value in enumerate(indegree) if value==0]
deleted = [False for x in range(n)]
q = collections.deque(node_with_in_zero)
result =[]
while q:
    front = q.popleft()
    result.append(front)
    for v in adj_list[front]:
        indegree[v]-=1
        if indegree[v]==0:
            q.append(v)
print(*result, sep=' ')

