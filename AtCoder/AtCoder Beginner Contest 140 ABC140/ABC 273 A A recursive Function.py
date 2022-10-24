def f(k):
    if k==0 or k==1:
        return 1
    return k*f(k-1)
    
n = int(input())
print(f(n))