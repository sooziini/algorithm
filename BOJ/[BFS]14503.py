# 로봇 청소기 - BFS

import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split())
r,c,d=map(int, sys.stdin.readline().split())
graph=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx,dy=[-1,0,1,0],[0,1,0,-1] # 북 동 남 서

def bfs(r,c,d):
    q=deque([(r,c,d)])
    visited=[[False]*m for _ in range(n)]
    visited[r][c]=True
    cnt=1
    while q:
        x,y,direc=q.popleft()
        for i in range(1,5):
            nx,ny=x+dx[(direc-i)%4],y+dy[(direc-i)%4]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0 and not visited[nx][ny]:
                q.append((nx, ny, (direc-i)%4))
                visited[nx][ny]=True
                cnt+=1
                break
        else:
            nx,ny=x+dx[(direc+2)%4],y+dy[(direc+2)%4]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=1:
                q.append((nx, ny, direc))
    return cnt

print(bfs(r,c,d))