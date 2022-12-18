n= int(input())
boss_arr = list(map(int, input().split()))
profit_vector = list(map(int, input().split()))

class Node:
    def __init__(self, data = None):
        self.employee_code = data
        self.direct_underlings = []
        self.team_profit = 0

nodeArray = [Node(x) for x in range(n+1)]
for index, boss in enumerate(boss_arr): 
    nodeArray[boss].direct_underlings.append(index+2)
def dfs_helper(node_idx):
    if node_idx<0 or node_idx>n:
        return 0
    node = nodeArray[node_idx]
    profit = profit_vector[node_idx-1]
    for x in node.direct_underlings:
        profit+= dfs_helper(x)
    node.team_profit = profit
    return profit  
max_profit = dfs_helper(1)
for i in range(2, n+1):
    if not nodeArray[i].direct_underlings:
        max_profit = max(max_profit, profit_vector[i-1])
    else:
        max_profit = max(max_profit, nodeArray[i].team_profit)
print(max_profit)