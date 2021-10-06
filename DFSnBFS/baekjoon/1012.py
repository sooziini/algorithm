# 유기농 배추

import sys
from collections import deque

q = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ret = []

def bfs(i, j):
    q.append((i, j))
    data[i][j] = 0
    while q:
        x, y = q.popleft()
        for t in range(4):
            nx = dx[t] + x
            ny = dy[t] + y
            if 0<=nx<n and 0<=ny<m and data[nx][ny] == 1:
                q.append((nx, ny))
                data[nx][ny] = 0

t = int(sys.stdin.readline().rstrip())  # 총 실행 횟수
for _ in range(t):
    cnt = 0
    m, n, k = map(int, sys.stdin.readline().split())
    data = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        data[x][y] = 1
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                bfs(i, j)
                cnt += 1
    ret.append(cnt)

for r in ret:
    print(r)