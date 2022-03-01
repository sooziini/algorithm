# 최단경로 - Dijkstra

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

v,e=map(int, input().split())
start=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    s,e,w=map(int, input().split())
    graph[s].append((e, w))     # s->e weight=w
distance=[INF]*(v+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))   # (거리, 현재 노드)
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for end, weight in graph[now]:
            cost=dist+weight
            if cost<distance[end]:
                distance[end]=cost
                heapq.heappush(q, (cost, end))

dijkstra(start)

for i in range(1, v+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])