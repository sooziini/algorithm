# 로봇 프로젝트 - BS

import sys

while True:
    try:
        x=int(sys.stdin.readline())*10000000
        n=int(sys.stdin.readline())
        blocks=sorted([int(sys.stdin.readline()) for _ in range(n)])
        left,right=0, n-1
        while left<right:
            total=blocks[left]+blocks[right]
            if total==x:
                print('yes %d %d' %(blocks[left], blocks[right]))
                break
            elif total<x:
                left+=1
            else:
                right-=1
        else:
            print('danger')
    except: # EOFError
        break