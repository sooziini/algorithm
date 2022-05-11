# 합승 택시 요금 (2021 KAKAO BLIND RECRUITMENT)

import heapq

INF=int(1e9)

def dijkstra(graph, start, end):
    n = len(graph)
    distance = [INF] * (n+1)
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for e, w in graph[now]:
            cost = dist + w
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (cost, e))
    return distance[end]

def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] * (n+1) for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    for i in range(1, n+1):
        answer = min(answer, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b))
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
