import collections
def floodFill(image, x, y, newColor):
    # Write your Code here.
    
    # We can choose to solve this, but first lets create an array of arrays for visited nodes.
    if not image:
        return None
    
    testColor = image[x][y]
    replacementColor = newColor
    visited=[[False for a in range(len(image[0]))] for b in range(len(image))]
    def isValid(nx, ny):
        if nx>=0 and ny>=0 and nx<len(image) and ny<len(image[0]):
            return True
        return False;
    q = collections.deque([(x,y)])
    while q:
        v = q.popleft()
        visited[v[0]][v[1]]=True
        if image[v[0]][v[1]]==testColor:
            image[v[0]][v[1]]=replacementColor
            neighbors = [(v[0]+1,v[1]),(v[0],v[1]+1),(v[0]-1,v[1]),(v[0],v[1]-1)]
            for nx, ny in neighbors:
                if isValid(nx, ny):
                    if not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny]=True
    return image