# 맥주 마시면서 걸어가기 - BFS

import sys
from collections import deque

def bfs():
    q = deque([home])
    visited = [0]*store_cnt
    while q:
        x, y = q.popleft()
        if abs(x-festival[0])+abs(y-festival[1])<=1000:
            return "happy"
        # 편의점을 들려야 하는 경우
        for i in range(store_cnt):
            if visited[i]==0 and abs(x-store[i][0])+abs(y-store[i][1])<=1000:
                q.append([store[i][0], store[i][1]])
                visited[i]=1
    return "sad"

t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    store_cnt = int(sys.stdin.readline())
    home = list(map(int, sys.stdin.readline().split()))
    store = [list(map(int, sys.stdin.readline().split())) for _ in range(store_cnt)]
    festival = list(map(int, sys.stdin.readline().split()))
    answer.append(bfs())

for a in answer:
    print(a)