# 퇴사

import sys

n = int(sys.stdin.readline())
t = []
p = []
dp = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    t.append(x)
    p.append(y)
    dp.append(y)
dp.append(0)

for i in range(n-1, -1, -1):
    if t[i]+i > n:      # 걸리는 시간+현재 일 > 전체 일 수
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])

print(dp[0])