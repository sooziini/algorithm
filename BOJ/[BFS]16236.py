# 아기 상어

import sys
from collections import deque

n=int(sys.stdin.readline())
data=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx,dy=[-1, 1, 0, 0],[0, 0, -1, 1]
fish_cnt=0  # 현재 먹을 수 있는 물고기의 수
eat_cnt=0   # 현재 먹은 물고기의 수
shark_size=2    # 아기 상어의 크기
time=0      # 현재 시간
for i in range(n):
    for j in range(n):
        if data[i][j]==9:   # 아기 상어 시작 위치
            shark_x,shark_y=i,j
        if 0<data[i][j]<=6:
            fish_cnt+=1     # 먹을 수 있는 물고기의 수 카운트
data[shark_x][shark_y]=0

def bfs(shark_x, shark_y):
    q=deque([(shark_x, shark_y, 0)])
    visited=[[False]*n for _ in range(n)]
    visited[shark_x][shark_y]=True
    edible_list=[]  # 먹을 수 있는 물고기의 위치를 저장하는 배열
    while q:
        x,y,distance=q.popleft()
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if data[nx][ny]<=shark_size:    # 지나갈 수 있는 경우
                    if 0<data[nx][ny]<shark_size:   # 물고기를 먹을 수 있는 경우
                        edible_list.append([distance+1, nx, ny])
                    else:
                        visited[nx][ny]=True
                        q.append((nx, ny, distance+1))
    if edible_list:
        return sorted(edible_list)[0]
    return False

while fish_cnt:
    cur=bfs(shark_x, shark_y)   # 현재 먹을 물고기 탐색 후 위치 리턴
    if not cur:     # 먹을 수 있는 물고기가 없을 경우
        break
    time+=cur[0]
    shark_x,shark_y=cur[1],cur[2]
    data[shark_x][shark_y]=0
    fish_cnt-=1
    eat_cnt+=1
    if shark_size==eat_cnt:
        shark_size+=1
        eat_cnt=0

print(time)