# 봄버맨 - 구현

import sys
input=sys.stdin.readline

r,c,n=map(int, input().split())
board=[list(input().rstrip()) for _ in range(r)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

if n==1:
    pass
elif n%2==0:
    board=[['O']*c for _ in range(r)]
else:
    for i in range(2):
        new_board=[['O']*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j]=='O':
                    new_board[i][j]='.'
                    for d in range(4):
                        nx,ny=i+dx[d],j+dy[d]
                        if 0<=nx<r and 0<=ny<c:
                            new_board[nx][ny]='.'
        board=new_board
        if n%4==3:
            break

for b in board:
    print(''.join(b))