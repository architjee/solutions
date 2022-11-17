# CodeForces Round 827 Div.4
# D.Coprime.py
import bisect
def main():
    n, q= map(int, input().split())
    heights_arr = list(map(int, input().split()))
    questions_arr = list(map(int, input().split()))

    prev = heights_arr[0]
    my_max_till_i = prev
    my_max_arr = [0 for i in range(n)]
    sum_till_i = [0]+[heights_arr[0] for i in range(n)]
    for index in range(0, n):
        my_max_till_i=max(heights_arr[index], my_max_till_i)
        my_max_arr[index]=my_max_till_i
        if not index:
            continue
        sum_till_i[index+1]=sum_till_i[index]+heights_arr[index]
    # print(my_max_arr, sum_till_i)
    result = [0 for i in range(len(questions_arr))]
    for index, step_size in enumerate(questions_arr):
        ans_idx =  bisect.bisect_right(my_max_arr, step_size)
        
        result[index] =sum_till_i[ans_idx] 
    print(*result, sep=' ')
t = int(input())
for _ in range(t):
    main()