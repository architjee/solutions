import math
x,y,a,b = map(int, input().split());
print(int(min(math.fabs(x-y), math.fabs(a-x)+math.fabs(y-b), math.fabs(a-y)+math.fabs(x-b))))
