'''
linked list node class for reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def reverseLL(head, low: int, high: int):
    # write your code here
    # Both the positions low and high are completly valid and must be reversed
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    dummy_head = Node(0)
    dummy_head.next = head
    subList_head = dummy_head
    for _ in range(1, low):
        subList_head = subList_head.next
    
    subList_iter = subList_head.next
    for _ in range(high-low):
        temp = subList_iter.next
        subList_head.next, subList_iter.next, temp.next = temp, temp.next, subList_head.next
    return dummy_head.next