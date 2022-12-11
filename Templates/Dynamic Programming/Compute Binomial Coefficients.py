# binomial coefficients are ncr


## Think of the recurrent relation for ncr.
## ncr = n-1cr-1 + n-1cr

## Can we come up with a solution on our own.
n, r = 4, 2
combinatorial_matrix = [[0]*(r+1) for x in range(n+1)]
def compute_n_c_r(n, r):
    if r==0:
        return 1
    if r==n:
        return 1
    if combinatorial_matrix[n][r]==0:
        ## We might have our base case.
        ## Let's first do recursion then will try caching the results.
        combinatorial_matrix[n][r] =  compute_n_c_r(n-1, r-1)+compute_n_c_r(n-1, r)
    return combinatorial_matrix[n][r]
print(compute_n_c_r(n, r))