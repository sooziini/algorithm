# 토마토

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())
box = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 익지 않은 토마토가 있는지 확인
# 다 익었다면 최소 날짜 return
def tmtChk():
    ret = -1
    for l in box:
        if 0 in l:
            return -1     # 익지 않은 토마토 있음
        ret = max(ret, max(l))
    return ret-1          # 최소 날짜

def bfs():
    while q:
        x, y = q.popleft()
        for t in range(4):
            nx = dx[t] + x
            ny = dy[t] + y
            if 0<=nx<n and 0<=ny<m and box[nx][ny]==0:
                box[nx][ny] = box[x][y]+1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))
bfs()
print(tmtChk())