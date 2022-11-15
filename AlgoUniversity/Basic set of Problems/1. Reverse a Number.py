def main():
    def reverse_number(n):
        result = []
        while n:
            result.append(str(n%10))
            n =n//10
        return ''.join(result)
    
        
    n = int(input())
    print(int(reverse_number(n)))
t = int(input())
for _ in range(t):
    main()