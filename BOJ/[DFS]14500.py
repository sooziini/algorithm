# 테트로미노 - DFS

import sys

n,m=map(int, sys.stdin.readline().split())
nums=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx,dy=[-1, 1, 0, 0],[0, 0, -1, 1]

def dfs(x, y, idx, sums):
    global answer
    if idx==3:
        answer=max(answer, sums)
        return
    if answer>=(3-idx)*max_value+sums:
        return
    for d in range(4):
        nx,ny=x+dx[d],y+dy[d]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=True
            if idx==1:  # 5th tetromino (ㅜ)
                dfs(x, y, idx+1, sums+nums[nx][ny])
            dfs(nx, ny, idx+1, sums+nums[nx][ny])
            visited[nx][ny]=False

answer=0
max_value=max(map(max, nums))
for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i, j, 0, nums[i][j])
        visited[i][j]=False

print(answer)