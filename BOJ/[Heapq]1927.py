# 최소 힙 - heapq!!!!

import sys, heapq

n=int(sys.stdin.readline())
answer=[]
hq=[]
for _ in range(n):
    cur_num=int(sys.stdin.readline())
    if cur_num==0:
        if hq:
            answer.append(heapq.heappop(hq))
        else:   # 현재 배열이 비어있을 경우
            answer.append(cur_num)
    else:   # x가 자연수일 경우
        heapq.heappush(hq, cur_num)
for a in answer:
    print(a)