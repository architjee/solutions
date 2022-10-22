h, w = map(int,input().split())
xArray = [0 for cols in range(w)]
for rows in range(h):
    thisRow = input()
    for index, x in enumerate(thisRow):
        if x=='#':
            xArray[index]+=1
for x in xArray:
    print(x, end=' ')