n = int(input())
listA =list( map(int, input().split()))
listA.sort()
for x in listA:
    print(x,end=' ')