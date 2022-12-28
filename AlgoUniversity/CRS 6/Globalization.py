from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


WHITE, BLACK = range(2)
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.color = WHITE

n, m =map(int, input().split())
node_array = [GraphNode(x) for x in range(n+1)]
for row_t in range(m):
    u , v = map(int, input().split())
    node_array[u].children.append(node_array[v])
    node_array[v].children.append(node_array[u])
@bootstrap
def dfs_helper(node):
    node.color = BLACK  
    for child in node.children:
        if child.color == WHITE:
            yield dfs_helper(child)
    yield 1


count = 0
for i in range(1, n+1):
    if node_array[i].color == WHITE:
        dfs_helper(node_array[i])
        count+=1
print(count-1)