
def binomial_coefficient(n, k):
    c_array = [0 for i in range(k+1)]
    c_array[0] = 1

    for i in range(1, n+1):
        j = min(i,k)
        while j:
            c_array[j] = c_array[j] + c_array[j-1]
            j-=1
    return c_array[k]

n, k = 5, 2
print(binomial_coefficient(n,k))