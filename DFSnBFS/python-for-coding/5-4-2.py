from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1, 1]
ret = 1

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로에서 벗어난 경우 무시
            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            # 벽인 경우 무시
            if (graph[nx][ny] == 0):
                continue
            # 새로운 좌표에 이전값+1 설정
            if (graph[nx][ny] == 1):
                graph[nx][ny] = 2
                global ret 
                ret += 1
                queue.append((nx, ny))
    return ret

print(bfs(0, 0))