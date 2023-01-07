t = int(input())
for t_it in range(t):
    n = int(input())
    fruits_array = list(map(int, input().split()))
    import collections
    my_fruits_counter = collections.Counter(fruits_array)
    print(len(my_fruits_counter))


## Test case
# 2
# 6
# 20 40 30 50 40 20
# 4
# 3 6 7 7

# Test case 1 answer
# 4
# 3


