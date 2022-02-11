# 멀티탭 스케줄링 - Greedy

import sys

n,k=map(int, sys.stdin.readline().split())
prods=list(map(int, sys.stdin.readline().split()))

if n>=k:
    print(0)
else:
    plug=[]
    cnt=0
    while prods:
        cur=prods.pop(0)
        if len(plug)<n and cur not in plug:
            plug.append(cur)
            continue
        if cur in plug:
            continue
        if len(plug)==1:
            plug[0]=cur
        else:
            priority=plug[:]
            for p in prods:
                if p in priority:
                    priority.remove(p)
                    if len(priority)==1:
                        break
            plug[plug.index(priority[0])]=cur
        cnt+=1
    print(cnt)