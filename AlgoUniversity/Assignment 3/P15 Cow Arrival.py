# P15 Cow Arrival.
n = int(input())
bigList = []
for x in range(n):
    aT, cT = map(int, input().split())
    bigList.append([aT, cT])


def getKey(obj):
    return obj[0]

time = 0
bigList.sort(key=getKey)
# Initialize time to zero.
for arrivalTime, checkUpTime in bigList:
    if time < arrivalTime:
        # The doctor will have to wait
        time = arrivalTime + checkUpTime
    else:
        # The cow will have to wait. Till doctor finishes and after time it has to spend CheckupTIme
        time += checkUpTime

print(time)
