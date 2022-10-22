from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    # We are supposed to sort the array in place
    # Good thing we are practicing this question.
    # We will have the following invariants
    # [:smaller] for <pivot element
    # [smaller: equal] for = pivot element
    # [equal: large] for unclassified element
    # [large: ] for large elements
    pivot = 1
    smaller, equal, large = 0, 0, len(arr)
    while equal < large:
        element = arr[equal]
        if element<pivot:
            # We must add this element to the smaller4
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller+=1
            equal+=1
        elif element == pivot:
            equal+=1
        else:
            large-=1
            arr[large], arr[equal] = arr[equal], arr[large]
         

#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
