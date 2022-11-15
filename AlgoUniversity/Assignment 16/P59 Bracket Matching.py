# You are given a bracket sequence of length N consisting of only '(' and ')'. Your task is to output an array of length N. The ith element in the array must be equal to the index of the corresponding bracket in the sequence of the ith bracket. If there is no corresponding bracket then the value in the array at that position should be -1. Please look at the sample testcase for a better understanding.
# EXAMPLE
# Sample 1 INPUT:
# text
# (())()
# Sample 1 OUTPUT:
# properties
# 3 2 1 0 5 4 
# Sample 2 INPUT:
# text
# )((()
# Sample 2 OUTPUT:
# diff
# -1 -1 -1 4 3
B_MAPPING = { '(': ')'} 
inp = input()
result = [-1 for _ in range(len(inp))]
stk = []
import collections
tup = collections.namedtuple('tup', ('element', 'index'))
for index, x in enumerate(inp):
    if x in B_MAPPING:
        # means it is an opening brace.
        stk.append(tup(x, index))
    else:
        # it is a closing brace
        if stk:
            popTup = stk.pop()
            if x==B_MAPPING[popTup.element]:
                result[index] = popTup.index
                result[popTup.index] = index
print(*result, sep=' ')
