"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        newRoot = Node(node.val)
        vertexMirror = {node: newRoot}
        q= collections.deque([node])
        while q:
            v=q.popleft()
            for neigh in v.neighbors:
                if neigh not in vertexMirror:
                    # We must creat a clone of this vertex
                    vertexMirror[neigh]=Node(neigh.val)
                    q.append(neigh)
                vertexMirror[v].neighbors.append(vertexMirror[neigh])
        return newRoot