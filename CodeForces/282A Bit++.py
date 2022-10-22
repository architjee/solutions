n = int(input())
x=0
for ops in range(n):
    statement =input()
    if statement=="X++" or statement=="++X":
        x+=1
    else:
        x-=1
print(x)