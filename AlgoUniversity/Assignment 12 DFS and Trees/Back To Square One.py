
WHITE, GRAY, BLACK = range(3)

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.goto_edges = []
        self.color = WHITE

n, m = map(int, input().split())
graph = [GraphNode(n) for x in range(n)]
for edge_t in range(m):
    u, v = map(int, input().split())
    graph[u].goto_edges.append(graph[v])
## We will solve this question using color theory

def detect_cycle(G):
    def has_cycle(cur):
        if cur.color == GRAY:
            return True
        cur.color= GRAY
        if any(next_node.color!=BLACK and has_cycle(next_node) for next_node in cur.goto_edges):
            return True
        cur.color = BLACK
        return False
    return any(node.color==WHITE and has_cycle(node) for node in G)

if detect_cycle(graph):
    print('NO')
else:
    print('YES')