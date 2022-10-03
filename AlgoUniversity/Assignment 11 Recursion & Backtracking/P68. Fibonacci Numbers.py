# Given an input number n. Output the nth fibonacci number.
n = int(input())
def fib(n):
    if(n<=2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))