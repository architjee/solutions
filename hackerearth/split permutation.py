t = int(input())
for t_it in range(t):
    n =int(input())
    a_array = list(map(int,input().split()))
    b_array = list(map(int,input().split()))
    a_set = set()
    b_set = set()
    i=0
    count = 0
    while i< n:
        if a_array[i]-b_array[i]>=0:
            count+=1
        i+=1
    print(count)
# TEST case 1
# 3
# 2
# 1 2
# 1 2
# 2
# 1 2
# 2 1
# 6
# 1 2 3 4 5 6
# 2 1 3 5 6 4