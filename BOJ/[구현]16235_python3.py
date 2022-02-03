# 나무 재테크 - 구현
# python3, pypy3 통과

import sys
from collections import defaultdict

n,m,k=map(int, sys.stdin.readline().split())
a=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
trees=[[defaultdict(int) for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z=map(int, sys.stdin.readline().split())
    trees[x-1][y-1][z]=1
cur_a=[[5]*n for _ in range(n)]
dx,dy=[-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

for _ in range(k):
    new_trees=[[defaultdict(int) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dead=0
            for age, cnt in sorted(trees[i][j].items()):
                tmp=cur_a[i][j]//age
                if tmp>=cnt:
                    cur_a[i][j]-=age*cnt
                    new_trees[i][j][age+1]=cnt
                    if (age+1)%5==0:
                        for d in range(8):
                            nx,ny=i+dx[d],j+dy[d]
                            if 0<=nx<n and 0<=ny<n:
                                new_trees[nx][ny][1]+=cnt
                elif 1<=tmp<cnt:
                    cur_a[i][j]-=age*tmp
                    new_trees[i][j][age+1]=tmp
                    dead+=(age//2)*(cnt-tmp)
                    if (age+1)%5==0:
                        for d in range(8):
                            nx,ny=i+dx[d],j+dy[d]
                            if 0<=nx<n and 0<=ny<n:
                                new_trees[nx][ny][1]+=tmp                       
                else:
                    dead+=(age//2)*cnt
            cur_a[i][j]+=a[i][j]+dead
    trees=new_trees

answer=0
for i in range(n):
    for j in range(n):
        for cnt in trees[i][j].values():
            answer+=cnt
print(answer)