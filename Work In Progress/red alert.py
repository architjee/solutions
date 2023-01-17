class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


n, c = map(int, input().split())
node_array = [TreeNode(x) for x in range(n + 1)]

is_red = [0] + list(map(int, input().split()))
for i in range(n - 1):
    u, v = map(int, input().split())
    # print(u, v, 'is uv')
    node_array[u].children.append(node_array[v])
result = []

def dfs(node, consecutive_red):
    if (is_red[node.val]==1):
        consecutive_red+=1
    else:
        consecutive_red= 0
    if consecutive_red>c:
        return 0
    total_leafs = 0
    for child in node.children:
        total_leafs += dfs(child, consecutive_red)
    if len(node.children)==0:
        total_leafs+=1  
    return total_leafs
if n==1:
    print(1)
else:
    print(dfs(node_array[1], 0))
