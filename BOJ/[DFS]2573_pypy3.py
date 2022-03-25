# 빙산 - DFS
# python3 시간초과 / pypy3 통과

from copy import deepcopy
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

n,m=map(int, input().split())
iceberg=[list(map(int, input().split())) for _ in range(n)]

dx,dy=[-1,1,0,0],[0,0,-1,1]

def find_first_loc():
    for i in range(1, n-1):
        for j in range(1, m-1):
            if iceberg[i][j]>0:
                return (i, j)

def dfs(x, y):
    iceberg[x][y]=-1
    for d in range(4):
        nx,ny=x+dx[d],y+dy[d]
        if iceberg[nx][ny]==0:
            if new_iceberg[x][y]>0:
                new_iceberg[x][y]-=1
        if iceberg[nx][ny]>0:
            dfs(nx, ny)

def chk_separate():
    for i in range(1, n-1):
        for j in range(1, m-1):
            if iceberg[i][j]>0:
                return True
    return False

year=0
while True:
    new_iceberg=deepcopy(iceberg)
    x,y=find_first_loc()
    dfs(x, y)
    if chk_separate():
        break
    if sum(map(sum, new_iceberg))==0:
        year=0
        break
    iceberg=new_iceberg
    year+=1
print(year)