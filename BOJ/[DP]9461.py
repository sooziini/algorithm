# 파도반 수열 - DP

import sys

t=int(sys.stdin.readline())
n_list=[int(sys.stdin.readline()) for _ in range(t)]

dp=[0]*101
dp[1],dp[2],dp[3],dp[4],dp[5]=1,1,1,2,2
for i in range(6, max(n_list)+1):
    dp[i]=dp[i-1]+dp[i-5]

for n in n_list:
    print(dp[n])