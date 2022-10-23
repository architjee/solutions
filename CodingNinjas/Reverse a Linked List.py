from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    # Write your code here.
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    dummy_head = sublist_head = Node(0)
    dummy_head.next = head
    sublist_head.next = head
    def getDepth(node):
        if not node:
            return 0
        size = 0
        while node:
            node = node.next
            size+=1
        return size
    finish = getDepth(dummy_head)-1
    # Using the generic Reverse Linked List template.
    start = 1
    for _ in range(1, start):
        sublist_head = sublist_head.next
        
    sublist_iter = sublist_head.next
    for _ in range(finish-start):
        temp = sublist_iter.next
        sublist_head.next, sublist_iter.next, temp.next = temp, temp.next, sublist_head.next
    return dummy_head.next
