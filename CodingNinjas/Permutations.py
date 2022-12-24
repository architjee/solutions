from os import *
from sys import *
from collections import *
from math import *

def permutations(vec, size):
    # Write your code here.
    result = []
    def helper_for_permutation(idx):
        if idx==size:
            result.append(vec[:])
        for j in range(idx, len(vec)):
            vec[idx], vec[j]= vec[j], vec[idx]
            helper_for_permutation(idx+1)
            vec[idx], vec[j]= vec[j], vec[idx]
    helper_for_permutation(0)
    return result
            
# Main.
t = int(input())
while t:
    n = int(input())
    sequenceOfNumbers = list(map(int, input().strip().split(" ")))
    answer = permutations(sequenceOfNumbers, n)
    answer.sort()
    for element in answer:
        print(*element, sep=' ', end=' ')
    print()
    t = t-1