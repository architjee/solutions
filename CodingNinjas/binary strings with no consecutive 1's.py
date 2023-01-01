from sys import stdin, setrecursionlimit
import sys
setrecursionlimit(10**6)

def generateString(k):
    # Write your code here.
    result = []
    def aux(idx, partial_sol):
        if idx==k-1:
            result.append(partial_sol[:])
            return
        if idx==0:
            partial_sol = '0'
            aux(idx+1, partial_sol)
            partial_sol = '1'
            aux(idx+1, partial_sol)
        elif idx>0:
            if partial_sol[-1]=='1':
                ## Can only choose zero
                aux(idx+1, partial_sol+'0')
            else:
                aux(idx+1, partial_sol+'0')
                aux(idx+1, partial_sol+'1')
    aux(0, '')
    return result








# Main.
t = int(input())
while t:
    n = int(input())
    answer = generateString(n)
    if len(answer) <= 0:
        t = t-1
        continue
    for x in answer:
        print(*x, sep='', end=' ')
    print()
    t = t-1
