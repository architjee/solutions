def main():
    s= input()
    def palindromne(s):
        return all(s[i]==s[~i] for i in range(len(s)//2))
    if palindromne(s):
        print("Yes")
    else:
        print("No")
t = int(input())
for _ in range(t):
    main()