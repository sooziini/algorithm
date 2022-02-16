# LCS (Longest Common Subequence) - DP

import sys

s1=sys.stdin.readline().rstrip()
s2=sys.stdin.readline().rstrip()

def lcs(s1, s2):
    dp=[["" for _ in range(len(s2))] for _ in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                if i==0 or j==0:
                    dp[i][j]=s1[i]
                else:
                    dp[i][j]=dp[i-1][j-1]+s1[i]
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1], key=len)
    return len(dp[-1][-1])

ans=lcs(s1, s2)
print(len(ans))
if len(ans)!=0:
    print(ans)