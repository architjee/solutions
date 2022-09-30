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