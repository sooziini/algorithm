# 특정한 최단 경로 - Dijkstra

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,e=map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1,v2=map(int, input().split())

def dijkstra(start):
    distance=[INF]*(n+1)
    q=[(0, start)]
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for e, w in graph[now]:
            cost=dist+w
            if cost<distance[e]:
                distance[e]=cost
                heapq.heappush(q, (cost, e))
    return distance

start_1=dijkstra(1)
start_v1=dijkstra(v1)
start_v2=dijkstra(v2)
ans=min(start_1[v1]+start_v1[v2]+start_v2[n], start_1[v2]+start_v2[v1]+start_v1[n])
print(ans if ans<INF else -1)