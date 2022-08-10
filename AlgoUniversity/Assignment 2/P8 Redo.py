# We are given tagetW
n, w = map(int,input().split())
bigList = list(map(int, input().split()))
idxArray = [-1]*1000002
for index, x in enumerate(bigList):
    idxArray[x] = index
possible = False
for index, x in enumerate(bigList):
    if x> w:
        continue
    else:
        wremaining = w -x
        if(idxArray[wremaining]!=-1) and index!= idxArray[wremaining]:
            print(idxArray[wremaining]+1, index+1)
            possible = True
            break
if(possible == False):
    print(-1)