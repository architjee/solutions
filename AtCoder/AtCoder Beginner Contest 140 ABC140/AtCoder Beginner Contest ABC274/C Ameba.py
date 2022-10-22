#TODO
class Node:
    def __init__(self, val):
        self.val = val
        self.left,self.right = None, None
# After seeing the editorial realized that it was a very simple problem with looked like heap, but is done via tree.
n = int(input())
tree = []
for node in map(int, input().split()):
    newNode = Node(node)
    tree.append(newNode)
print(tree)