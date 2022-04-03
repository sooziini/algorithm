# 최소비용 구하기 - Dijkstra

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    s,e,weight=map(int, input().split())
    graph[s].append((e, weight))
start,end=map(int, input().split())
distance=[INF]*(N+1)

def dijkstra(s):
    q=[]
    heapq.heappush(q, (0, s))
    distance[s]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for e, weight in graph[now]:
            cost=dist+weight
            if cost<distance[e]:
                distance[e]=cost
                heapq.heappush(q, (cost, e))

dijkstra(start)
print(distance[end])