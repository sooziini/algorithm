# 미네랄 - BFS

from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
turn = list(map(int, input().split()))
dx, dy = [1,-1,0,0], [0,0,-1,1]

def is_even(n):
    if n % 2 == 0:
        return True    # even
    return False     # odd

def bfs(i, j):
    q = deque([(i, j)])
    visited = [[False] * C for _ in range(R)]
    visited[i][j] = True
    fall_list = []
    while q:
        x, y = q.popleft()
        if x == R-1:
            return False
        fall_list.append((x, y))
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] == 'x' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    fall(fall_list, visited)
    return True

def fall(fall_list, visited):
    fall_cnt = int(1e9)
    for x, y in fall_list:
        cnt = 0
        for i in range(x+1, R):
            if cave[i][y]=='x':
                break
            cnt += 1
        if not visited[i][y]:
            fall_cnt = min(fall_cnt, cnt)
    if 0 < fall_cnt < int(1e9):
        for x, y in sorted(fall_list, reverse=True):
            cave[x][y] = '.'
            cave[x+fall_cnt][y] = 'x'

for idx, t in enumerate(turn):
    cur = cave[R-t]
    for i, c in enumerate(cur if is_even(idx) else cur[::-1]):
        if c == 'x':
            x, y = R-t, i if is_even(idx) else C-i-1
            cave[x][y]='.'
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] == 'x':
                    if bfs(nx, ny):
                        break
            break

for idx, c in enumerate(cave):
    print(''.join(c), end='\n' if idx+1 < len(cave) else '')