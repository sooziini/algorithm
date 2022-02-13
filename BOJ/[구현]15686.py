# 치킨 배달 - 구현

import sys, math
from itertools import combinations

n,m=map(int, sys.stdin.readline().split())
city=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

chickens,homes=[],[]
for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            homes.append((i, j))
        if city[i][j]==2:
            chickens.append((i, j))

ans=math.inf
for combi in combinations(chickens, m):
    total=0
    for hx, hy in homes:
        dist=abs(hx-combi[0][0])+abs(hy-combi[0][1])
        for cx, cy in combi[1:]:
            dist=min(dist, abs(hx-cx)+abs(hy-cy))
        total+=dist
    ans=min(ans, total)
print(ans)