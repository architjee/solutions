def mainFunc():
    n = int(input())
    # n is <=8
    notPresent = map(int, input().split())
    # we need to print 10-nC2*6
    def c(n):
        return int(n*(n-1)/2)
    print(c(10-n)*6)

t = int(input())
for testcase in range(t):
    mainFunc()