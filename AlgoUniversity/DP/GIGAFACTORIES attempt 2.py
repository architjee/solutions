n, max_cost = map(int, input().split())
cost_array = []
profit_array = []
for i in range(n):
    cost, profit = map(int, input().split())
    cost_array.append(cost)
    profit_array.append(profit)
profit_matrix = [[0]*(max_cost+1) for p in range(2)]
if max_cost<=0:
    print(0)
else:
    def maximize_profit_under_max_cost(item_idx, max_cost):
        for item_idx in range(1, n):
            for allowed_cost in range(1,max_cost+1):
                ## Becuase we have to consider == cost.                                         
                profit_matrix[1][allowed_cost] = max(profit_matrix[1][allowed_cost-1]if cost_array[item_idx]>allowed_cost else profit_array[item_idx]+profit_matrix[1][allowed_cost-1], profit_matrix[0][allowed_cost])
                                                                                                                                                                                        ## Don't consider that item and 
            profit_matrix[0]= profit_matrix[1].copy()

        return profit_matrix
    print(maximize_profit_under_max_cost(n-1, max_cost))