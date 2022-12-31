    from os import *
    from sys import *
    from collections import *
    from math import *

    ## Ops
    def main(n, weights, prices, max_capacity):
        d ={}
        def extract_max_price(ending_idx, avail_capacity):
            if avail_capacity<=0:
                return 0
            if ending_idx<0:
                return 0
            without_this_item = 0
            with_this_item = 0
            key = (ending_idx, avail_capacity)
            if key not in d:
                if avail_capacity>=weights[ending_idx]:
                    with_this_item = prices[ending_idx]+ extract_max_price(ending_idx-1, avail_capacity- weights[ending_idx])
                without_this_item = extract_max_price(ending_idx-1, avail_capacity)
                d[key]= max(without_this_item, with_this_item)
            return d[key]
        print(extract_max_price(n-1 , max_capacity))


    ## Read input as specified in the question.
    t = int(input())
    for t_it in range(t):
        n = int(input())
        weights = list(map(int,input().split()))
        prices = list(map(int, input().split()))
        max_capacity = int(input())
        main(n, weights, prices, max_capacity)

    ## Print output as specified in the question.
