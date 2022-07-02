# Only seem to be passing the first test case.
# Finding lower bound in the array;
# Finding the upper bound in the array:


n= int(input());
bigList = list(map(int, input().split()));
Q = int(input());
for q in range(Q):
    x = int(input());
    lbRes = -1;
    low = 0;
    high = n-1
    while low<=high:
        mid = (low+high)//2;
        if(bigList[mid]==x):
            #save the result
            lbRes = mid;
            # But still go low.
            high = mid-1;
        elif(bigList[mid]>x):
            high = mid -1 ;

        else: 
            low = mid+1;
    upRes = -1;
    low = 0;
    high = n-1;
    while low<=high: 
        mid =( low+high)//2;
        if(bigList[mid]==x):
            #save the result 
            upRes = mid;
            # but go up 
            low = mid+1;
        elif(bigList[mid]>x):
            high = mid - 1;
        else :
            low = mid+1
    print(lbRes, upRes);