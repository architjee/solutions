#input vala section
# We are given n
from platform import node


n = int(input())

bossArray = list(map(int, input().split()))
class Node:
    def __init__(self, data = None):
        self.key = data
        self.child = []
        self.underlings = 0
 
i = 2
nodeArray = [Node(x) for x in range(n+1)]
for x in bossArray: 
    nodeArray[x].child.append(nodeArray[i])
    i+=1
# We might implement some sort of DFS here:
def dfsChildUnder(node, parent):
    
    if(node==None):
        return 0
    peopleUnderNode=0
    
    for x in node.child:
        if x!=parent:
            peopleUnderNode += dfsChildUnder(x, node)
    node.underlings= peopleUnderNode
    return peopleUnderNode+1
dfsChildUnder(nodeArray[1], -1)
for x in range(1, n+1):
    print(nodeArray[x].underlings, end=" ")




