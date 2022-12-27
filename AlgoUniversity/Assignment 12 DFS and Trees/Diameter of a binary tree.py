n = int(input())

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.goto_edges = []

nodearray = [GraphNode(x) for x in range(n)]
for edges_it in range(n-1):
    u , v = map(int,input().split())
    u-=1
    v-=1
    nodearray[u].goto_edges.append(nodearray[v])

def height(subtree):
    if subtree == None:
        return 0
    heights_arr = [height(child_node) for child_node in  subtree.goto_edges]
    if not heights_arr:
        heights_arr = [0]
    return 1 + max(heights_arr)

def diameter(subtree):
    if subtree==None:
        return 0
    heights_arr = [height(child_node) for child_node in  subtree.goto_edges]
    