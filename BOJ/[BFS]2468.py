# 안전 영역 - BFS

import sys
from collections import deque

n=int(sys.stdin.readline())
area=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def get_max(area):
    maxi=0
    for a in area:
        maxi=max(maxi, max(a))
    return maxi

def set_visited(area, num):
    visited=[[True]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j]<=num:
                visited[i][j]=False
    return visited

dx,dy=[-1, 1, 0, 0],[0, 0, -1, 1]
def bfs(i, j, visited):
    q=deque([(i, j)])
    visited[i][j]=False
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]:
                visited[nx][ny]=False
                q.append((nx, ny))

answer=[]
for m in range(0, get_max(area)+1):
    visited=set_visited(area, m)
    cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                bfs(i, j, visited)
                cnt+=1
    answer.append(cnt)

print(max(answer))