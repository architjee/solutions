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
    if not head or head.next==None:
        return head
    nodeMon = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return nodeMon
    # We don't really know if this function works or not, because of stackOverflow in CodingNinjas.