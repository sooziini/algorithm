# 가장 빠른 거리

import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())
sh, sw = map(int, sys.stdin.readline().split())
eh, ew = map(int, sys.stdin.readline().split())

def bfs():
    q = deque([(sh, sw, 0)])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    data = [[False] * (w + 1) for _ in range(h + 1)]
    data[sh][sw] = True
    while q:
        x, y, cnt = q.popleft()
        if x == eh and y == ew:
            return cnt
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 < nx <= h and 0 < ny <= w and data[nx][ny] == False:
                data[nx][ny] = True
                q.append((nx, ny, cnt + 1))
print(bfs())
