# 청소년 상어 - DFS

import sys
from copy import deepcopy

fish=[]
fish_dict={}
for _ in range(4):
    tmp=list(map(int, sys.stdin.readline().split()))
    tmp_list=[]
    for i in range(0, 8, 2):
        tmp_list.append(tmp[i])
        fish_dict[tmp[i]]=tmp[i+1]-1
    fish.append(tmp_list)

dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(fish, num):
    for row_idx, row in enumerate(fish):
        if num in row:
            return (row_idx, row.index(num))
    return None

def move_fishes(fish, fish_dict, shark_x, shark_y):
    for f in range(1, 17):
        pos=find_fish(fish, f)
        if pos==None:
            continue
        x,y=pos
        for d in range(8):
            fish_direc=(fish_dict[f]+d)%8
            nx,ny=dx[fish_direc]+x,dy[fish_direc]+y
            if 0<=nx<4 and 0<=ny<4 and not (nx==shark_x and ny==shark_y):
                fish[x][y],fish[nx][ny]=fish[nx][ny],fish[x][y]
                fish_dict[f]=fish_direc
                break

def get_shark_positions(fish, x, y, direc):
    positions=[]
    for d in range(1, 4):
        nx,ny=dx[direc]*d+x,dy[direc]*d+y
        if 0<=nx<4 and 0<=ny<4 and fish[nx][ny]>0:
            positions.append((nx, ny))
    return positions

def dfs(fish, fish_dict, shark_x, shark_y, cnt):
    shark_direc=fish_dict[fish[shark_x][shark_y]]
    cnt+=fish[shark_x][shark_y]
    fish[shark_x][shark_y]=0

    move_fishes(fish, fish_dict, shark_x, shark_y)

    positions=get_shark_positions(fish, shark_x, shark_y, shark_direc)
    
    if len(positions)==0:
        global answer
        answer=max(answer, cnt)
        return
    for nx, ny in positions:
        dfs(deepcopy(fish), deepcopy(fish_dict), nx, ny, cnt)

answer=0
dfs(fish, fish_dict, 0, 0, 0)
print(answer)