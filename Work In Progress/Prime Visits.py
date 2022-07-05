def isValid():
    pass
t = int(input())
for i in range(t):
    count = 0   
    a,b = map(int, input());
    for x in range(a, b+1):
        if isValid(x):
            count+=1