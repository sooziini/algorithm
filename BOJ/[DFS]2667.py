# 단지 번호 붙이기 - DFS

import sys

n = int(sys.stdin.readline())
apart = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False]*n  for _ in range(n)]

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return
    if apart[x][y] == '1' and visited[x][y] == False:
        global num
        num += 1
        visited[x][y] = True
        # 해당 위치에서 상하좌우 위치 모두 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return

cnt = 0     # 총 아파트 단지 수
num = 0     # 각 단지내 집의 수
ret = []
for i in range(n):
    for j in range(n):
        if apart[i][j] == '1' and visited[i][j] == False:
            dfs(i, j)
            cnt += 1
            ret.append(num)
            num = 0

print(cnt)
for n in sorted(ret):
    print(n)