from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import json

def partition(s):
    # Write your code here.
    result = []
    def directed_partition(offset, partial_partition):
        if offset==len(s):
            result.append(partial_partition.copy())
        for i in range(offset+1, len(s)+1):
            prefix = s[offset: i]
            if prefix == prefix[::-1]:
                directed_partition(i, partial_partition+[prefix])
    directed_partition(0, [])
    return result
s=stdin.readline().rstrip()

final=partition(s)

for ele in final:
    ele = sorted(ele)
    print(json.dumps(ele))
