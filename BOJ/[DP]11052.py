# 카드 구매하기 - DP

import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)
dp[1] = card[0]
for i in range(2, n+1):
    for j in range(0, i):
        dp[i] = max(dp[i], dp[j]+card[i-1-j])
print(dp[n])

# dp[2] = dp[0]+card[1] or dp[1]+card[0]
# dp[3] = dp[0]+card[2] or dp[1]+card[1] or dp[2]+card[0]