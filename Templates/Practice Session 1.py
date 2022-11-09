# Converting string to binary
int("1010101", base=2)

# Converting int to binary string.
bin(7).replace('0b','')

iterable = [1,2,3,4,4]
# Use of enumerate
for index, value in enumerate(iterable):
    print(index, value)

d={1:"Alpha", 2:"Beta"}
for key, value in d.items():
    print(key , value)

# General Linked List template
class ListNode:
    def __init__(self, data=0, next=None):
        self.data= data
        self.next = next

# Check if a string is a plaindromne in Python
s = "hello"
def check_palindronme(s):
    return all(s[i]==s[~i] for i in range(len(s)//2))

import functools, string
# Evaluate num_as_string in base b1
# Given base=b1
b1=4
num_as_string= "1321"
is_negative = num_as_string[0]=="-"
num_as_int = functools.reduce(
    lambda val, c: val*b1 + string.hexdigits.index(c),
     num_as_string[is_negative:], 0
    
)