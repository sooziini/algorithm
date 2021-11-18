n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if (x < 0 or x >= n or y < 0 or y >= m):
        return False

    # 값이 0이면 0을 2로 바꾸고 상하좌우 dfs 실행
    if (graph[x][y] == 0):
        graph[x][y] = 2
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    return False

ret = 0
for i in range(n):
    for j in range(m):
        if (dfs(i, j)):
            ret += 1

print(ret)