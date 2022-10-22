from typing import *
import collections
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        testColor = image[sr][sc]
        replacementColor = color
        visited=[[False for a in range(len(image[0]))] for b in range(len(image))]
        def isValid(nx, ny):
            if nx>=0 and ny>=0 and nx<len(image) and ny<len(image[0]):
                return True
            return False;
        q = collections.deque([(sr,sc)])
        while q:
            v = q.popleft()
            visited[v[0]][v[1]]=True
            if image[v[0]][v[1]]==testColor:
                image[v[0]][v[1]]=replacementColor
                neighbors = [(v[0]+1,v[1]),(v[0],v[1]+1),(v[0]-1,v[1]),(v[0],v[1]-1)]
                for nx, ny in neighbors:
                    if isValid(nx, ny):
                        print("Did we approve of these", nx, ny , " and is valid said", isValid(nx, ny))
                        if not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny]=True
        return image