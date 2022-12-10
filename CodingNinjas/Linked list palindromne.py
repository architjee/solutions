from os import *
from sys import *
from collections import *
from math import *

# List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


def isPalindrome(head):
    # I think we should stop using none altogether and focus only on the .data field !=-1
    if head==None or head.data==-1:
        return True
    data_tracker = []
    while head and head.data!=-1:
        data_tracker.append(head.data)
        head = head.next
    def check_palidromne(arr):
        return all(arr[i]==arr[~i] for i in range(len(arr)//2))
    return check_palidromne(data_tracker)