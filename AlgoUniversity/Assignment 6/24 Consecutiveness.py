n = int(input())
bigList = list(map(int, input().split()))
bigList.sort()
prev = bigList[0]
answer = 1  
# Now we will traverse in the array from 1st position.
length = 1
for i in range(1, n):

    currentElement = bigList[i]
    if currentElement==prev:
        # Total Ignore.
        pass
    elif currentElement== prev+1:
        length += 1
        answer = max(answer, length)
        prev = currentElement
    else :
        # Reset the length to 1.
        length=1
        prev =currentElement
print(answer)