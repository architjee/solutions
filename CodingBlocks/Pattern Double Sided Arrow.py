n = int(input())

x = 0
midSpace = -6
while x< ((n//2)+1):
    print("    "*(n//2-x), end='')
   
    temp = x+1;
    while temp:
        print(temp, end=' ')
        temp -=1
    temp = 1
    midSpace += 4
    for t in range(midSpace):
        print(" ", end='')
    if x ==0 :
        x+=1
        print()
        continue
    while temp<=x+1:
        print(temp, end=' ')
        temp +=1
    print()
    x+=1
x-=2
while x>=0:
    print("    "*(n//2-x), end='')
   
    temp = x+1;
    while temp:
        print(temp, end=' ')
        temp -=1
    temp = 1
    midSpace -= 4
    for t in range(midSpace):
        print(" ", end='')
    if x ==0 :
        x-=1
        print()
        continue
    while temp<=x+1:
        print(temp, end=' ')
        temp +=1
    print()
    x-=1
    