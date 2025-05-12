# 아이템 줍기
# 2배 스케일링.. 처음 들어봄

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1] * 102 for _ in range(102)]

    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, rec)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x == x2 or x == x1 or y == y2 or y == y1:
                    if graph[x][y] != 0:
                        graph[x][y] = 1 # 테두리
                else:
                    graph[x][y] = 0 # 내부
    
    q = deque([(characterX * 2, characterY * 2, 0)])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = True
    while q:
        x, y, cnt = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = cnt // 2
            break
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 1 <= nx < 102 and 1 <= ny < 102 and graph[nx][ny] == 1 and not visited[nx][ny]: 
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
