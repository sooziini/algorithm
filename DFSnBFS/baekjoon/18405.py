# 경쟁적 전염

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
virus = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while q:
        v, a, b, time = q.popleft()
        if time >= s:        # 시간 초과 확인
            break
        for t in range(4):
            na = dx[t] + a
            nb = dy[t] + b
            if 0<=na<n and 0<=nb<n and virus[na][nb]==0:
                virus[na][nb] = v
                q.append((virus[na][nb], na, nb, time+1))

qList = []
for i in range(n):
    for j in range(n):
        if virus[i][j]>0:
            qList.append((virus[i][j], i, j, 0))
qList.sort()
q = deque(qList)
bfs()

print(virus[x-1][y-1])