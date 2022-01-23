# 안전 영역 - BFS

import sys
from copy import deepcopy
from collections import deque

n=int(sys.stdin.readline())
area=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def get_max(area):
    maxi=0
    for a in area:
        maxi=max(maxi, max(a))
    return maxi

def change_area(area, num):
    for i in range(n):
        for j in range(n):
            if area[i][j]<=num:
                area[i][j]=0
    return area

dx,dy=[-1, 1, 0, 0],[0, 0, -1, 1]
def bfs(i, j, area):
    q=deque([(i, j)])
    area[i][j]=0
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<n and area[nx][ny]!=0:
                area[nx][ny]=0
                q.append((nx, ny))

answer=[]
for m in range(0, get_max(area)+1):
    area_copy=change_area(deepcopy(area), m)
    cnt=0
    for i in range(n):
        for j in range(n):
            if area_copy[i][j]!=0:
                bfs(i, j, area_copy)
                cnt+=1
    answer.append(cnt)

print(max(answer))