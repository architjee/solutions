n, m =map(int, input().split());
lst = list(map(int, input().split()));
d={};
for x in range(len(lst)):
    d[lst[x]]=x
lst.sort();
for x in range(len(lst)):
    currElement = lst[x];
    result = -1;    
    low = x + 1;
    high = n-1;
    target = m - currElement
    result = -1
    while(low<=high):
        mid = (low + high) //2;
        if(lst[mid]==target and mid!=x):
            result = mid;
            break;
        elif lst[mid]>target:
            high = mid -1;
        elif lst[mid]<target:
            low = mid+1
    if(result != -1):
        print(d[currElement]+1, d[lst[result]]+1);
        break;
else:
    print(-1)