def largestNumber (N):
    # Write your code here
    pass
    num_as_string = str(N)
    num_as_string = num_as_string.replace('X', 'A', 1)
    total_sum =0
    for each_char in num_as_string:
        if each_char=='A' or each_char=='X':
            continue
        else:
            total_sum += int(each_char)
    prev_answer = ''
    for x in range(10):
        for y in range(10):
            final_sum =  total_sum+  + y
            new_answer = num_as_string.replace('A',str(x)).replace('X',str(y))
            if final_sum%3==0 and final_sum%9!=0 and new_answer>prev_answer:
                prev_answer =  new_answer
    print(prev_answer)

N = input()

out_ = largestNumber(N)
print (out_)