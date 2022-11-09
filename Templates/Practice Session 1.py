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

# Solve Look and say problem:
def look_and_say(n):
    def next_number(s):
        i ,count =0, 1
        result=[]
        while i<len(s):
            while i+1<len(s) and s[i]==s[i+1]:
                i+=1
                count+=1
            result.append(str(count)+s[i])
            i+=1
            count=1
        return ''.join(result)
    s='1'
    for _ in range(1, n):
        s = next_number(s)
    return s

# Implement construct from base functino
def construct_from_base(num_as_int, base):
    return '' if num_as_int ==0 else construct_from_base(num_as_int//base, base) + string.hexdigits[num_as_int%base].upper()

# Implment spreadsheet column encoding . 
def spreadsheet_decode_col_id(col):
    return functools.reduce(lambda result, c : result*26 + ord(c)-ord('A')+1, col, 0)

# Implement reverse all words in a sentence
def reverse_words_in_a_sent(sentence):
    sentence.reverse()

    def reverse_range(iter, start, end):
        while start<end:
            iter[start], iter[end] = iter[end], iter[start]
            start, end=start+1, end-1
    start = 0
    while True:
        end = sentence.find(' ', start)
        if end<0:
            break
        reverse_range(sentence, start, end-1)
        start=end+1
    reverse_range(sentence, start, len(s)-1)