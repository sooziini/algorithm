# 캐슬 디펜스 - 구현

import sys
from itertools import combinations

n,m,d=map(int, sys.stdin.readline().split())
enemies=[]
for i in range(n):
    data=list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if data[j]==1:
            enemies.append([i, j])

def move_enemies(old):
    new=[]
    for i in range(len(old)):
        if old[i][0]<n-1:
            new.append([old[i][0]+1, old[i][1]])
    return new

def play_game(cur_enemies):
    cnt=0
    while cur_enemies:
        candidate=set()
        for x, y in combi:
            possible=[]
            for ex, ey in cur_enemies:
                dist=abs(ex-x)+abs(ey-y)
                if dist<=d:
                    possible.append((dist, ex, ey))
            if possible:
                possible.sort(key=lambda x:(x[0], x[2], -x[1]))
                candidate.add((possible[0][1], possible[0][2]))
        for cx, cy in candidate:
            cnt+=1
            cur_enemies.remove([cx, cy])
        cur_enemies=move_enemies(cur_enemies)
    return cnt

ans=0
for combi in list(combinations([(n, i) for i in range(m)], 3)):
    ans=max(ans, play_game([e[:] for e in enemies]))
print(ans)