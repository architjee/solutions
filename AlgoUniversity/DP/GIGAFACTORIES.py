n, max_cost = map(int, input().split())
cost_array = []
profit_array = []
for i in range(n):
    cost, profit = map(int, input().split())
    cost_array.append(cost)
    profit_array.append(profit)
profit_matrix = [[-1]*(max_cost+1) for p in profit_array]
if max_cost<=0:
    print(0)
else:
    def maximize_profit_under_max_cost(item_idx, max_cost):
        ## We are going to write a recursive solution and optimize it.
        if item_idx<0:
            return 0
            ## Can't generate profit if item_idx. As no more elments can be added.
        if profit_matrix[item_idx][max_cost]==-1:
            ## Notyet processed.
            profit_wihtout_this_item = maximize_profit_under_max_cost(item_idx-1, max_cost)
            if cost_array[item_idx]>max_cost:
                profit_with_this_item= 0
            else:
                profit_with_this_item = profit_array[item_idx]+maximize_profit_under_max_cost(item_idx-1, max_cost-cost_array[item_idx])
            profit_matrix[item_idx][max_cost] = max(profit_wihtout_this_item, profit_with_this_item)
        return profit_matrix[item_idx][max_cost]

    print(maximize_profit_under_max_cost(n-1, max_cost))