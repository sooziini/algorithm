# 다리 놓기 - 조합

import sys

t=int(sys.stdin.readline())

for _ in range(t):
    n,m=map(int, sys.stdin.readline().split())
    ans=1
    for i in range(n):
        ans*=(m-i)
    for i in range(n-1):
        ans//=(n-i)
    print(ans)