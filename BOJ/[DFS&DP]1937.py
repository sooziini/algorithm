# 욕심쟁이 판다 - DFS & DP

import sys
# 런타임 에러 (RecursionError 방지)
# 재귀 허용 깊이를 늘려야 함 recurtion depth
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
bamboo = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dp = [[0]*n for _ in range(n)]

def dfs(x, y):
    if dp[x][y] < 1:    # 이미 방문한 곳이라면 원래 값 리턴
        dp[x][y] = 1    # 현재 위치 1로 설정
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<n and 0<=ny<n and bamboo[x][y]<bamboo[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)     # 원래 왔던 경로 하나 더하기
    return dp[x][y]

ret = 0
for i in range(n):
    for j in range(n):
        ret = max(ret, dfs(i, j))
print(ret)