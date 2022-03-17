# 꽃길 - DFS

import sys
input=sys.stdin.readline
MAX_VALUE=20000

n=int(input())
costs=[list(map(int, input().split())) for _ in range(n)]

dx,dy=[-1,1,0,0],[0,0,-1,1]
visited=[[False]*n for _ in range(n)]
min_cost=MAX_VALUE

def chk_visited(x, y):
    for d in range(4):
        if visited[x+dx[d]][y+dy[d]]:
            return True
    return False

def reset_visited(x, y):
    visited[x][y]=False
    for d in range(4):
        visited[x+dx[d]][y+dy[d]]=False

def calc_cost(x, y):
    cost=costs[x][y]
    visited[x][y]=True
    for d in range(4):
        nx,ny=x+dx[d],y+dy[d]
        visited[nx][ny]=True
        cost+=costs[nx][ny]
    return cost

def dfs(i, depth, res):
    if depth==3:
        global min_cost
        min_cost=min(min_cost, res)
        return
    for x in range(i, n-1):
        for y in range(1, n-1):
            if not visited[x][y] and not chk_visited(x, y):
                dfs(x, depth+1, res+calc_cost(x, y))
                reset_visited(x, y)
dfs(1, 0, 0)
print(min_cost)