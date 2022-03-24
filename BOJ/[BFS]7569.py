# 토마토 - BFS

from collections import deque
import sys
input=sys.stdin.readline

m,n,h=map(int, input().split())
tomato=[]
chk=deque()
for z in range(h):
    tmp=[list(map(int, input().split())) for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if tmp[x][y]==1:
                chk.append((x, y, z))
    tomato.append(tmp)

dx,dy,dz=[-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]

def bfs():
    global chk
    new_chk=deque()
    while chk:
        x,y,z=chk.popleft()
        for d in range(6):
            nx,ny,nz=x+dx[d],y+dy[d],z+dz[d]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h and tomato[nz][nx][ny]==0:
                tomato[nz][nx][ny]=1
                new_chk.append((nx, ny, nz))
    chk=new_chk
    return new_chk

def chk_zero(tomato):
    for to in tomato:
        for t in to:
            if t.count(0):
                return False
    return True

ret=0
while bfs():
    ret+=1
print(ret if chk_zero(tomato) else -1)