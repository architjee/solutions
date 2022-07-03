# Given nxm matrix
n,m = map(int, input().split());
bigList =  [];
for i in range(n):
    bigList.extend(list(map(int, input().split())));
x = int(input())
bigSet = set(bigList)
if x in bigSet:
    print(1);
else:
    print(0);
