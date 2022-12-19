
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTree(preOrder, inOrder, n) :
    #Your code goes here
    ## THe first node in preorder is the rootf 
    def helper(preorder, inorder):
        if not preorder or not inorder:
            return None
        if len(preorder)==1 and len(inorder)==1:
            return BinaryTreeNode(preorder[0])
        newNode = BinaryTreeNode(preorder[0])
        index, val = 0, None
        for index, val in enumerate(inorder):
            if val==preorder[0]:
                break
        
        newNode.left = helper(preorder[1:index+1], inorder[:index+1])
        newNode.right = helper(preorder[index+1:], inorder[index+1:])
        return newNode
    return helper(preOrder, inOrder)




































'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# Main
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)
