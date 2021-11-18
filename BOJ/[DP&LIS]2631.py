# 줄세우기 - DP & LIS

import sys

n = int(sys.stdin.readline())
child = [int(sys.stdin.readline()) for _ in range(n)]

# LIS
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if child[i] > child[j]:     # 현재 위치 값 > 전 위치 값
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))