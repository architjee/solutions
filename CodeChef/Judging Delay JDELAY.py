# cook your dish here
def mainFun():
    count = 0
    n= int(input())
    for iter in range(n):
        subTime , judgeTime = map(int,input().split())
        if judgeTime-subTime>5:
            count+=1
    print(count)
t= int(input())
for _ in range(t):
    mainFun()
