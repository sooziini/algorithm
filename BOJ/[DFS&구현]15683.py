# 감시 - DFS & 구현

import sys
from copy import deepcopy

n,m=map(int, sys.stdin.readline().split())
office,cctv=[],[]
for i in range(n):
    office.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if 0<office[i][j]<6:
            cctv.append((office[i][j], i, j))

def count_zero(office):
    ret=0
    for o in office:
        ret+=o.count(0)
    return ret

def change_office(new_office, direc, x, y):
    for d in direc:
        for i in range(1, n*m):
            nx,ny=x+(dx[d]*i),y+(dy[d]*i)
            if 0<=nx<n and 0<=ny<m and new_office[nx][ny]<6:
                if new_office[nx][ny]==0:
                    new_office[nx][ny]=-1
            else:
                break
    return new_office

dx,dy=[-1,0,1,0],[0,-1,0,1]
cctv_direc=[[],[[0],[1],[2],[3]],
            [[0,2],[1,3]],
            [[0,1],[1,2],[2,3],[3,0]],
            [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
            [[0,1,2,3]]]

def dfs(depth, office):
    if depth==len(cctv):
        global ans
        ans=min(ans, count_zero(office))
        return
    num,x,y=cctv[depth]
    for direc in cctv_direc[num]:
        dfs(depth+1, change_office(deepcopy(office), direc, x, y))

ans=n*m
dfs(0, office)
print(ans)