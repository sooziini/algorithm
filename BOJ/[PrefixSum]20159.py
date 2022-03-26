# 동작 그만. 밑장 빼기냐? - 누적합

import sys
input=sys.stdin.readline

n=int(input())
cards=[0]+list(map(int, input().split()))

odds,evens=[0],[0]
for i in range(1, n+1):
    if i%2:
        odds.append(cards[i]+odds[-1])
        evens.append(evens[-1])
    else:
        odds.append(odds[-1])
        evens.append(cards[i]+evens[-1])
ret=odds[-1]
for i in range(1, n+1):
    if i%2:
        ret=max(ret, odds[i-1]+(evens[-1]-evens[i]))
    else:
        ret=max(ret, odds[i]+(evens[-2]-evens[i-1]))
print(ret)