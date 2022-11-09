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
     num_as_string[is_negative:], 
     0
)

# Convert int to string in python
def convert_int_to_string(x):
    if x<0:
        x = -x
        is_negative = True
    result = []
    while True:
        result.append(chr(ord('0')+x%10))
        x = x//10
        if x==0:
            break
    return ('-' if is_negative else '') + ''.join(reversed(result))

def convert_string_to_int(num_as_string):
    if not num_as_string:
        return 0
    is_negative=False
    result = 0
    base = 10
    for c in num_as_string:
        if c=='-':
            is_negative=True
            continue
        result = result*base + (ord(c)-ord('0'))
    if is_negative:
        return result*(-1)
    return result



# Convert from base b1 to base b2
def convert_b1_to_b2(num_as_string, b1, b2):
    if num_as_string[0]=='-':
        is_negative=True
    num_as_int = functools.reduce(
        lambda val, c: val*b1+string.hexdigits.index(c.lower()), num_as_string[is_negative:], 0
    )
    def construct_from_base(num_as_int, base):
        return '' if num_as_int==0 else construct_from_base(num_as_int//base, base)+string.hexdigits[num_as_int%base].upper()
    return ('-' if is_negative else '')+('0' if num_as_int==0 else construct_from_base(num_as_int, b2))
