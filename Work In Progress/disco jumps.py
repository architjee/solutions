import collections
n, m = map(int, input().split())
Coordinate = collections.namedtuple('Coordinate', ('i', 'j', 'arrangement') )
matrix = [[Coordinate(0,0,())]*m for x in range(n)]
for i in range(n):
    for j in range(m):
        colors = input().split()
        matrix[i][j]=Coordinate(i, j, tuple(colors))
print('finally the matrix is ', matrix)
def is_valid_coordinate(x, y):
    if x>=0 and x<m and y>=0 and  y<n:
        return True
    return False
def bfs():
    visited = [False for x in range(n)]
    q = collections.deque([matrix[0][0]])
    while q:
        front = q.popleft()
        for x,y in ((front.i+1, front.j),(front.i, front.j+1)):
            if is_valid_coordinate(x, y):
                pass

