from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:

class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def leastCommonAncestor(n1, n2):
    # Write your code here.
    
    # Write your code here.
    ## We will traverse to root from n1
    ## Handle edge cases at the end of the problem.
    height1 = 0
    runner = n1
    while runner!=None and runner.parent!=None:
        runner = runner.parent
        height1+=1
    runner = n2
    height2 = 0
    while runner!=None and runner.parent!=None:
        runner = runner.parent
        height2 += 1
    # Now the difference in height will decide which node should travel more.
    if height1>height2:
        n1,n2 = n2, n1
        height1, height2 = height1, height2
    # Travel the distance diff height in height 2
    runner2 = n2
    for k in range(height2-height1):
        runner2= runner2.parent
    
    while n1!=runner2:
        n1=n1.parent
        runner2 = runner2.parent
    return n1