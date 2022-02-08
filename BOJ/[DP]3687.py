# 성냥개비 - DP

import sys

t=int(sys.stdin.readline())
n_list=[int(sys.stdin.readline()) for _ in range(t)]

mini=[0]*101
mini[2],mini[3],mini[4],mini[5],mini[6],mini[7],mini[8]=1,7,4,2,6,8,10
for i in range(9, max(n_list)+1):
    mini[i]=mini[i-2]*10+mini[2]
    for j in range(3,8):
        tmp=mini[j] if j!=6 else 0
        mini[i]=min(mini[i], mini[i-j]*10+tmp)

for n in n_list:
    maxi='7'*(n%2)+'1'*(n//2-(n%2))
    print(mini[n], maxi)