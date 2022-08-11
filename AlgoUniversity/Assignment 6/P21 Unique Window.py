n, k = map(int, input().split())
bigList = list(map(int, input().split()))
# Instantiate first size of window
d={}
for i in range(k):
    element = bigList[i]
    if element in d:
        d[element]+=1
    else:
        d[element]=1
start = 0
end = k-1
print(len(d), end=" ")
for i in range(n-k):
    # Print the sum of current window

    # Now we must prepare the sum for next window
    # We must add the end+1 element in d.
    end += 1
    endElement = bigList[end]
    if endElement in d:
        d[endElement]+=1
    else:
        d[endElement]=1
    startElement = bigList[start]

    if d[startElement]==1:
        d.pop(startElement)
    else:
        d[startElement]-=1
    start+=1
    print(len(d), end=" ")
    # We must remove the start element in d.
