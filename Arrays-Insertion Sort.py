n = int(input());
bigList = list(map(int, input()));

sortedTill = 0;
while sortedTill<n:
    # The array is sorted from 0 to sortedTill indexes.
    nextElement = bigList[sortedTill+1]
    # Now try to place the next element in places 0 to sorted+1
    i = sortedTill
    while nextElement< bigList[i] and i>=0:
        bigList[i+1] = bigList[i];
        i-=1;
    # This must be the index
    if(i<0):
        i=0;
    bigList[i] = nextElement