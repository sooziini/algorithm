# 나무 재테크 - 구현
# python3 시간초과 / pypy3 통과

import sys
from collections import deque

n,m,k=map(int, sys.stdin.readline().split())
a=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
trees=[[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z=map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(z)
cur_a=[[5]*n for _ in range(n)]
dx,dy=[-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

for _ in range(k):
    breed=[]
    for i in range(n):
        for j in range(n):
            new_age=deque()
            dead=0
            for age in trees[i][j]:
                if cur_a[i][j]>=age:
                    cur_a[i][j]-=age
                    new_age.append(age+1)
                    if (age+1)%5==0:
                        breed.append((i,j))
                else:
                    dead+=age//2
            trees[i][j]=new_age
            cur_a[i][j]+=a[i][j]+dead
    for i, j in breed:
        for d in range(8):
            nx,ny=i+dx[d],j+dy[d]
            if 0<=nx<n and 0<=ny<n:
                trees[nx][ny].appendleft(1)

answer=0
for i in range(n):
    for j in range(n):
        answer+=len(trees[i][j])
print(answer)