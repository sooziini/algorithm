# 미세먼지 안녕! - 구현

import sys

r,c,t=map(int, sys.stdin.readline().split())
home=[list(map(int, sys.stdin.readline().split())) for _ in range(r)]
air_cleaner=0
for i in range(r):
    if home[i][0]==-1:
        air_cleaner=i
        break

def spread():
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    new_home=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            new_home[i][j]+=home[i][j]
            if home[i][j]>=5:
                dust=home[i][j]//5
                for d in range(4):
                    nx,ny=i+dx[d],j+dy[d]
                    if 0<=nx<r and 0<=ny<c and home[nx][ny]!=-1:
                        new_home[nx][ny]+=dust
                        new_home[i][j]-=dust
    return new_home

def circulator():
    global home
    # TOP
    for i in range(air_cleaner-1, 0, -1):
        home[i][0]=home[i-1][0]
    for i in range(c-1):
        home[0][i]=home[0][i+1]
    for i in range(air_cleaner):
        home[i][c-1]=home[i+1][c-1]
    for i in range(c-1, 1, -1):
        home[air_cleaner][i]=home[air_cleaner][i-1]
    # BOTTOM
    for i in range(air_cleaner+2, r-1):
        home[i][0]=home[i+1][0]
    for i in range(c-1):
        home[r-1][i]=home[r-1][i+1]
    for i in range(r-1, air_cleaner+1, -1):
        home[i][c-1]=home[i-1][c-1]
    for i in range(c-1, 1, -1):
        home[air_cleaner+1][i]=home[air_cleaner+1][i-1]
    home[air_cleaner][1]=home[air_cleaner+1][1]=0

for _ in range(t):
    home=spread()
    circulator()

print(sum(map(sum, home))+2)