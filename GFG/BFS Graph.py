#User function Template for python3
from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        traversal = []
        visited = [False for x in adj]
        q = deque()
        q.append(0)
        while q:
            front = q.popleft()
            visited[front] = True
            traversal.append(front)
            for nodes in adj[front]:
                if not visited[nodes]:
                    visited[nodes] = True
                    q.append(nodes)
                    
                
        return traversal

