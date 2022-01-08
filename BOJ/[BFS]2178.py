# 미로 탐색 - BFS

import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split())
maze=[list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dx,dy=[-1, 1, 0, 0],[0, 0, -1, 1]

def bfs():
    q=deque([(0, 0, 1)])    # 미로 시작점과 이동 횟수(1부터 시작)
    visited=[[False]*m for _ in range(n)]
    visited[0][0]=True
    while q:
        x,y,cnt=q.popleft()
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1 and not visited[nx][ny]:
                if nx==n-1 and ny==m-1:     # 미로 도착점에 도착했을 경우
                    return cnt+1
                q.append((nx, ny, cnt+1))
                visited[nx][ny]=True
print(bfs())