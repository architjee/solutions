def combSum(ARR, B):

    # Write your code here
    # Return a list of sorted lists/combinations
    ## We are given target B
    ## Also the array of numbers is ARR.
    dp_array = [[[]]+[[]]*B for x in ARR]
    for i in range(len(ARR)):
        for j in range(1, B+1):
            ## We have to target B inclusive
            without_this_element = []
            if i>=1:
                without_this_element = dp_array[i-1][j]
            with_this_element = []
            if j>ARR[i]:
                for combination in dp_array[i][j-ARR[i]]:
                    with_this_element.append(combination+[ARR[i]])
            elif j==ARR[i]:
                with_this_element = [[ARR[i]]]
            dp_array[i][j] = without_this_element + with_this_element
    ans = dp_array[-1][-1]
    for seq in ans:
            seq.sort()
    return ans
        