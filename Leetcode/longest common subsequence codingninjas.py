
from sys import stdin

def lcs(s, t) :
    
    dp = {}
    def auxlcs(idx1, idx2):
        key = (idx1, idx2)
        if idx1<0 or idx2<0:
            return 0
        if key not in dp:
            if s[idx1]==t[idx2]:
                dp[key]= 1+ auxlcs(idx1-1, idx2-1)
            else:
                dp[key] =max( auxlcs(idx1-1, idx2), auxlcs(idx1, idx2-1))
        return dp[key]
    return auxlcs(len(s)-1, len(t)-1)





























    


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))