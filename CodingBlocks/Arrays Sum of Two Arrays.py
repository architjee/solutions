# Test Case
# 4
# 1 0 2 9
# 5
# 3 4 5 6 7
n = int(input());
listA = list(map(int, input().split()));
m = int(input());
listB = list(map(int, input().split()));
if (m>n):
    listA, listB = listB, listA;
    m,n = n,m
# Now always n>m
carry = 0;
tail  = -1;
res = []
while tail >= -n:
    tempSum = carry;
    tempSum += listA[tail];
    if(tail >= -m):
        tempSum += listB[tail];
    tempSum, carry = tempSum%10, tempSum//10
    res.append(tempSum)
    tail -= 1;
if(carry):
    res.append(carry);
for i in range(len(res)):
    print(res[len(res)-i-1], end = ', ')
print("END")

