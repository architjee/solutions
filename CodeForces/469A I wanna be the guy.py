n = int(input())
p, *pList = map(int, input().split())
q, *qList = map(int, input().split())
mainSet = set()
for x in pList:
    mainSet.add(x)
for x in qList:
    mainSet.add(x)
if(len(mainSet)==n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
