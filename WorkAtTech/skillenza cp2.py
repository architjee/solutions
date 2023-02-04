class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
nums = list(map(int,  input().split()))
def create_linked_list(array):
    head = None
    prev = None
    for index, x in enumerate(array):
        if index==0:
            ## Different processing
            prev = Node(x)
            head = prev
        else:
            new_node = Node(x)
            prev.next = new_node
            prev = prev.next
    return head
def print_linked_list(ll_head):
    curr = ll_head
    while curr!=None:
        print(curr.val,end=' ')
        curr = curr.next
def remove_duplicates_in_linked_list(ll_head):
    curr = ll_head
    prev = None
    while curr!=None:
        if not prev:
            ## We are seeing the first element, 
            prev = curr
        else:
            ## We have atleast one element.
            
            while curr and (curr.val==prev.val):
                curr = curr.next
            prev.next = curr
            prev = prev.next
        if not curr:
            break
        curr = curr.next
def main(nums):
    head = create_linked_list(nums)
    remove_duplicates_in_linked_list(head)
    print_linked_list(head)
if not nums:
    print('')
else:
    main(nums)