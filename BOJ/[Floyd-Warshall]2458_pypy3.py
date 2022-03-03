# 키 순서 - Floyd-Warshall

import sys
input=sys.stdin.readline

n,m=map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    graph[a][b]=1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k]+graph[k][b]==2:
                graph[a][b]=1

cnt=0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            continue
        if graph[a][b]+graph[b][a]==0:
            break
    else:
        cnt+=1
print(cnt)