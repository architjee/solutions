from os import *
from sys import *
from collections import *
from math import *

def getLengthOfLCS(str1, str2):
    # Write your code here.
    dp = {}
    def auxlcs(idx1, idx2):
        key = (idx1, idx2)
        if idx1<0 or idx2<0:
            return 0
        if key not in dp:
            if str1[idx1]==str2[idx2]:
                dp[key]= 1+ auxlcs(idx1-1, idx2-1)
            else:
                dp[key] =max( auxlcs(idx1-1, idx2), auxlcs(idx1, idx2-1))
        return dp[key]
    return auxlcs(len(str1)-1, len(str2)-1)