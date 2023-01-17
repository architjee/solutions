n, maximum_cost=map(int,input().split())

cost_array = [0 for x in range(n)]
profit_array = [0 for x in range(n)]
for i in range(n):
    cost, profit = map(int, input().split())
    cost_array[i]=cost
    profit_array[i]=profit
matrix = [[0]*(maximum_cost+1) for i in range(n+1)]
for i in range(n+1):
    for j in range(maximum_cost+1):
        if j==0 or i==0:
            matrix[i][j]=0
        elif j>=cost_array[i-1]:
            matrix[i][j]=max(matrix[i-1][j], profit_array[i-1]+matrix[i-1][j-cost_array[i-1]])
        else:
            matrix[i][j]=matrix[i-1][j]

print(matrix[-1][-1])