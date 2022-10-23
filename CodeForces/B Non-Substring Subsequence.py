#TODO This question 
def mainFunc():
    def isThereASubsequenceEqualToThisSubstring(bigString , substring):

    n, q= map(int, input().split())
    s= input()
    for query in range(q):
        l, r = map(int, input().split())
        if isThereASubsequenceEqualToThisSubstring(s, s[l-1,r]):
            print("YES")
        else:
            print("NO")
    pass
t = int(input())
for testCase in range(t):
    mainFunc()