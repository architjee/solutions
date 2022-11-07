def string_to_int(s):
    is_negative=False    
    partial_sum = 0
    for index, cha in enumerate(s):
        if cha=='-' and index==0:
            is_negative=True
            continue
        partial_sum*=10
        partial_sum+=ord(cha)-ord('0')
    if is_negative:
        return partial_sum*(-1)
    return partial_sum
