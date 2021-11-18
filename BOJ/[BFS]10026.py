# 적록색약

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
rgb = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(i, j):
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for t in range(4):
            nx = dx[t] + x
            ny = dy[t] + y
            if 0<=nx<n and 0<=ny<n and rgb[nx][ny]==rgb[x][y] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

def calc():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] is False:
                bfs(i, j)
                cnt += 1
    return cnt

# 색약 아닐 경우
visited = [[False]*n for _ in range(n)]
ret = calc()

# 색약일 경우
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if rgb[i][j] == 'R':
            rgb[i][j] = 'G'
rett = calc()

print(ret, rett)