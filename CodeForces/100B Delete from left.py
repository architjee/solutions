sList =list(input())
tList = list(input())
i=0
while i<len(sList) and i<len(tList):
    if sList[len(sList)-i-1]==tList[len(tList)-i-1]:
        i+=1
    else:
        break
print(len(sList)+len(tList)-(2*i))