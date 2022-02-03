# 주사위 굴리기 - 구현

import sys

n,m,x,y,k=map(int, sys.stdin.readline().split())
graph=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
orders=list(map(int, sys.stdin.readline().split()))

dx,dy=[0,0,-1,1],[1,-1,0,0]
dice=[0]*6  # back, top, front, bottom, left, right

for order in orders:
    nx,ny=x+dx[order-1],y+dy[order-1]
    if not (0<=nx<n and 0<=ny<m):
        continue
    if order==1:
        dice[1],dice[3],dice[4],dice[5]=dice[4],dice[5],dice[3],dice[1]
    elif order==2:
        dice[1],dice[3],dice[4],dice[5]=dice[5],dice[4],dice[1],dice[3]
    elif order==3:
        dice[0],dice[1],dice[2],dice[3]=dice[1],dice[2],dice[3],dice[0]
    elif order==4:
        dice[0],dice[1],dice[2],dice[3]=dice[3],dice[0],dice[1],dice[2]
    if graph[nx][ny]==0:
        graph[nx][ny]=dice[3]
    else:
        dice[3]=graph[nx][ny]
        graph[nx][ny]=0
    x,y=nx,ny
    print(dice[1])