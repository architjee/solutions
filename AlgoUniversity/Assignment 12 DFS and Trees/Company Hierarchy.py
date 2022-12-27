import sys
 
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
 
 
 
n = int(sys.stdin.readline())
adjacency_list_dir = [[] for i in range(n+1)]
manages = [0 for i in range(n+1)]
arr=[]
if n!=1:
    arr = [int(i) for i in sys.stdin.readline().split()]
for i in range(len(arr)):
    adjacency_list_dir[arr[i]].append(i+2)
#print(adjacency_list_dir)
 
@bootstrap
def dfs(curr):
    global adjacency_list_dir
    global manages
    sum = 0
    for i in adjacency_list_dir[curr]:
        sum+= yield dfs(i)
    manages[curr]=sum
    yield sum+1
 
dfs(1)
 
for i in range(1,n+1):
    print(manages[i],end=' ')