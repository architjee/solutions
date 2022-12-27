"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mirror = {None: None}
        mirror[head] = Node(head.val)
        curr = head
        while curr:
            if curr not in mirror:
                mirror[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr not in mirror:
                mirror[curr] = Node(curr.val)
            mirror[curr].next = mirror[curr.next]
            mirror[curr].random = mirror[curr.random]
            curr = curr.next
        return mirror[head]