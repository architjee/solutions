# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # I think this question seems like the standar merge k sorted arrays problem, which we can solve via heap.
        if not lists:
            return
        # We are also given multiple lists in the variable lists.
        import heapq
        min_heap = []

        for index, each_list in enumerate(lists):
            if each_list != None:
                heapq.heappush(min_heap, each_list.val)
                lists[index] = each_list.next
        flag = True
        dummy_head = ListNode(0)
        runner = dummy_head
        while min_heap and flag:
            flag = False 
            for index, each_list in enumerate(lists):
                if each_list!=None:
                    flag=True
                    heapq.heappush(min_heap, each_list.val)
                    lists[index] = each_list.next

        while min_heap:
            smallest = heapq.heappop(min_heap)
            runner.next = ListNode(smallest)
            runner = runner.next
        return dummy_head.next