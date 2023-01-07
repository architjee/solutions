class GraphNode:
    def __init__(self, val):
        self.val = val
        self.associations = []
t = int(input())
for t_it in range(t):
    n, q = map(int, input().split())
    ## We need to create a graph with n nodes
    node_array = [GraphNode(x) for x in range(n)]
    for q_it in range(q):
        query = list(map(int,input().split()))
        if query[0]==1:
            a ,b = query[1]-1, query[2]-1
            if node_array[b] not in node_array[a].associations:
                node_array[a].associations.append(node_array[b])
            if node_array[a] not in node_array[b].associations:
                node_array[b].associations.append(node_array[a])
        elif query[0]==2:
            a = query[1]-1
            ## Print connected component of a. 
        elif query[0]==3:
            a ,b = query[1]-1, query[2]-1
            ## Remove all existing associations of a and move them to b

# SAMPLE INPUT
# 2
# 4 3
# 1 1 2
# 3 2 3
# 2 3
# 3 2
# 2 1
# 2 2


## Sample output
# 2 5
# 1 1
# 1 2