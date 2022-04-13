# 양과 늑대 (2022 KAKAO BLIND RECRUITMENT)

from collections import defaultdict
from copy import deepcopy

is_wolf = list()
num_edges = defaultdict(list)
max_sheep = 0

def find_max_sheep(cur_node, nums, visited, possible):
    global max_sheep
    if visited[cur_node]:
        return
    visited[cur_node] = True
    nsheep, nwolf = nums
    if is_wolf[cur_node]:
        nwolf += 1
    else:
        nsheep += 1
        max_sheep = max(max_sheep, nsheep)
    if nsheep <= nwolf:
        return
    possible.extend(num_edges[cur_node])
    for next_node in possible:
        find_max_sheep(next_node, (nsheep, nwolf), deepcopy(visited), 
                possible=[p for p in possible if p != next_node and not visited[p]])

def solution(info, edges):
    global is_wolf, num_edges, max_sheep
    is_wolf = info
    visited = [False] * len(info)
    for start, end in edges:
        num_edges[start].append(end)
    find_max_sheep(0, (0, 0), visited, [])
    return max_sheep

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))