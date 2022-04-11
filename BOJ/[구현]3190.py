# 뱀 - 구현

import sys
input = sys.stdin.readline

N = int(input())
board = [[False]*N for _ in range(N)]
for _ in range(int(input())):
    i, j = map(int, input().split())
    board[i-1][j-1] = True
snake_info = {}
for _ in range(int(input())):
    X, C = input().split()
    snake_info[int(X)] = 1 if C == 'D' else -1

snake = [(0, 0)]
time, direc = 0, 0
dx, dy = [0,1,0,-1], [1,0,-1,0]

while True:
    time += 1
    nx, ny = snake[-1][0] + dx[direc], snake[-1][1] + dy[direc]
    if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in snake:
        break
    if board[nx][ny]:   # 사과有
        board[nx][ny] = False
    else:
        snake.pop(0)
    snake.append((nx, ny))
    if time in snake_info:
        direc = (direc + snake_info[time]) % 4
        snake_info.pop(time)
print(time)