# 분산처리 - 구현

import sys

t = int(sys.stdin.readline())
testcase = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

for a, b in testcase:
    ret = pow(a, b, 10)
    if ret==0:
        ret += 10
    print(ret)