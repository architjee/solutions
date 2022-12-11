def number_of_ways(n, m):
    ## x is the row we need to reach,
    ## y is the column we are targeting.
    no_of_routes_matrix = [[0]* m for _ in range(n)]
    def count_ways_util(x, y):
        if x==0 and y==0:
            return 1
            ## There is only 1 way to reach origin.

        if no_of_routes_matrix[x][y]==0:
            ## This means it is unprocessed.
            ways_bottom = 0 if x==0 else count_ways_util(x-1, y)
            ways_right = 0 if y==0 else count_ways_util(x, y-1)
            no_of_routes_matrix[x][y] = ways_bottom+ways_right
        return no_of_routes_matrix[x][y]
    
    return count_ways_util(n-1, m-1)