# 디지털 티비

import sys

n = int(sys.stdin.readline())
channel = [sys.stdin.readline().rstrip() for _ in range(n)]

ret = ''
kbs1 = channel.index('KBS1')
kbs2 = channel.index('KBS2')

# 1과 4만으로 나타내는 방법
ret += '1'*(kbs1)
ret += '4'*(kbs1)
if kbs1>kbs2:
    kbs2 += 1
ret += '1'*(kbs2)
ret += '4'*(kbs2-1)

print(ret)