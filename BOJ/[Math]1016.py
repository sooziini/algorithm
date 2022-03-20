# 제곱 ㄴㄴ수 - 에라토스테네스의 체

import sys

mini,maxi=map(int, sys.stdin.readline().split())

chk=[True]*(maxi-mini+1)
i=2
while i**2<=maxi:
    num=mini//(i**2)
    while num*(i**2)<=maxi:
        if mini<=num*(i**2)<=maxi:
            chk[num*(i**2)-mini]=False
        num+=1
    i+=1
print(chk.count(True))