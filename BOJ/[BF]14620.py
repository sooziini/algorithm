# 꽃길 - BruteForce

from itertools import combinations
import sys
input=sys.stdin.readline
MAX_VALUE=20000

n=int(input())
costs=[list(map(int, input().split())) for _ in range(n)]

candidate=[]
for i in range(1, n-1):
    for j in range(1, n-1):
        candidate.append((i, j))

min_cost=MAX_VALUE
dx,dy=[-1,1,0,0],[0,0,-1,1]
for combi in combinations(candidate, 3):
    visited=list(combi)
    tmp=0
    for x, y in combi:
        tmp+=costs[x][y]
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            visited.append((nx, ny))
            tmp+=costs[nx][ny]
    if len(set(visited))==15:
        min_cost=min(min_cost, tmp)
print(min_cost)