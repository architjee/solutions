
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
    
    node_to_inorder_index = { value: index for index, value in enumerate(inOrder)}
    def helper(p_start, p_end, in_start, in_end):
        if p_end<p_start or in_end<in_start:
            return None
        newNode = BinaryTreeNode(preOrder[p_start])
        if p_start==p_end and in_start==in_end:
            return newNode
        index, value = p_start, preOrder[p_start]
        inorder_idx_for_root=node_to_inorder_index[ preOrder[p_start]]
        left_size = inorder_idx_for_root-in_start
        newNode.left = helper(p_start+1, p_start+1+left_size, in_start, inorder_idx_for_root-1)
        newNode.right = helper(p_start+1+left_size, p_end, inorder_idx_for_root+1, in_end)
        return newNode
    return helper(0, len(preOrder)-1, 0, len(inOrder)-1)































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
