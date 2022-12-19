from sys import stdin
import  queue
# Following is the BinaryTreeNode class structure.
class BinaryTreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderSuccesor(root, node):
    # Write your code here.
    result = []
    def helper(subtree, node):
        if not subtree:
            return
        helper(subtree.left,node)
        result.append(subtree.data)
        helper(subtree.right,node)
    helper(root,node)
    for index, value in enumerate(result):
        if value==node:
            break
    if index+1<len(result):
        return result[index+1]
    return None

def buildTree(arr):
    if len(arr) == 0 or arr[0] == -1:
        return None
    root = BinaryTreeNode(arr[0])
    q = queue.Queue()
    q.put(root)
    i = 0
    while q.empty() is False:
        curr = q.get()
        i = i + 1
        if arr[i] != -1:
            left_Node = BinaryTreeNode(arr[i])
            curr.left = left_Node
            q.put(curr.left)

        i = i + 1
        if arr[i] != -1:
            right_Node = BinaryTreeNode(arr[i])
            curr.right = right_Node
            q.put(curr.right)

    return root

# Main Code.
t = int(input())

for i in range(t):
    arr = [int(i) for i in input().strip().split()]
    node = int(input().strip())

    root = buildTree(arr)
    ans = inorderSuccesor(root, node)

    if ans is None:
        print("NULL")

    else:
        print(ans)
