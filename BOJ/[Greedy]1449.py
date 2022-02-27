# 수리공 항승 - Greedy

import sys

n,l=map(int, sys.stdin.readline().split())
data=sorted(list(map(int, sys.stdin.readline().split())))

cnt=1
if n>1:
    i,j=0,1
    while j<n:
        if data[j]-data[i]>=l:
            i=j
            cnt+=1
        j+=1
print(cnt)