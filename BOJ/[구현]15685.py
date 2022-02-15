# 드래곤 커브 - 구현

import sys

n=int(sys.stdin.readline())

data=[[0]*101 for _ in range(101)]
dx,dy=[1,0,-1,0],[0,-1,0,1]

for _ in range(n):
    x,y,d,g=map(int, sys.stdin.readline().split())
    nx,ny=x+dx[d],y+dy[d]
    data[x][y]=data[nx][ny]=1
    x,y=nx,ny
    move=[d]
    for _ in range(g):
        tmp=[(t+1)%4 for t in move[::-1]]
        for t in tmp:
            nx,ny=x+dx[t],y+dy[t]
            data[nx][ny]=1
            x,y=nx,ny
        move.extend(tmp)
cnt=0
for i in range(100):
    for j in range(100):
        if data[i][j] and data[i+1][j] and data[i][j+1] and data[i+1][j+1]:
            cnt+=1
print(cnt)     