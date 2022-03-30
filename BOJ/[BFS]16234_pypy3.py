# 인구 이동 - BFS
# python3 시간초과 / pypy3 통과

from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

n,l,r=map(int, input().split())
people=[list(map(int, input().split())) for _ in range(n)]

visited=[[False]*n for _ in range(n)]
dx,dy=[-1, 1,0,0],[0,0,-1,1]

def move_people(change, num):
    new_people=num//len(change)
    for i, j in change:
        people[i][j]=new_people

def bfs(i, j, ver):
    q=deque([(i, j)])
    visited[i][j]=ver
    num=people[i][j]
    change=[(i, j)]
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]!=ver and l<=abs(people[x][y]-people[nx][ny])<=r:
                visited[nx][ny]=ver
                num+=people[nx][ny]
                change.append((nx, ny))
                q.append((nx, ny))
    if len(change)>1:
        move_people(change, num)

ret=0
ver=False
while True:
    cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==ver:
                bfs(i, j, not ver)
                cnt+=1
    if cnt==n*n:
        break
    ret+=1
    ver=not ver
print(ret)