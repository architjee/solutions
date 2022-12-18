n= int(input())
boss_arr = list(map(int, input().split()))

class Node:
    def __init__(self, data = None):
        self.employee_code = data
        self.direct_underlings = []
        self.team_size = 0

nodeArray = [Node(x) for x in range(n+1)]
for index, boss in enumerate(boss_arr): 
    if index>n:
        break
    nodeArray[boss].direct_underlings.append(index+2)
def dfs_helper(node_idx):
    node = nodeArray[node_idx]
    team_size = 0
    for x in node.direct_underlings:
        team_size+= dfs_helper(x)
    node.team_size = team_size+1
    return team_size+1
dfs_helper(1)
for i in range(1, n+1):
    print(nodeArray[i].team_size-1 ,end=' ')
print()