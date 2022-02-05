# 이모티콘 - BFS

import sys
from collections import deque

s=int(sys.stdin.readline())

def bfs():
    q=deque([(1, 0)])
    visited=[[0]*(s+1) for _ in range(s+1)]
    while q:
        e,c=q.popleft()
        if visited[e][e]==0:
            visited[e][e]=visited[e][c]+1
            q.append((e, e))
        if e+c<=s and visited[e+c][c]==0:
            visited[e+c][c]=visited[e][c]+1
            q.append((e+c, c))
        if e-1>0 and visited[e-1][c]==0:
            visited[e-1][c]=visited[e][c]+1
            q.append((e-1, c))
    return min([v for v in visited[s] if v!=0])

print(bfs())