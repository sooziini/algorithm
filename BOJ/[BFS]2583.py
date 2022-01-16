# 영역 구하기 - BFS

import sys
from collections import deque

m,n,k=map(int, sys.stdin.readline().split())    # 세로, 가로, 직사각형 개수
rectangle=[[0]*n for _ in range(m)]
dx,dy=[-1, 1, 0, 0],[0, 0, -1, 1]
for _ in range(k):
    x1,y1,x2,y2=map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            rectangle[i][j]=1   # 직사각형 영역을 1로 변환

def bfs(i, j):
    q=deque([(i, j)])
    rectangle[i][j]=1
    cnt=1   # 현재 분리된 영역의 넓이
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<m and 0<=ny<n and rectangle[nx][ny]==0:
                rectangle[nx][ny]=1
                cnt+=1
                q.append((nx, ny))
    return cnt

cnt_list=[]     # 분리된 영역의 넓이를 담을 배열
for i in range(m):
    for j in range(n):
        if rectangle[i][j]==0:
            cnt_list.append(bfs(i, j))
print(len(cnt_list))
for c in sorted(cnt_list):
    print(c, end=' ')