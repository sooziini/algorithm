# 안테나 - Sorting

import sys

n=int(sys.stdin.readline().rstrip())
data=sorted(list(map(int, sys.stdin.readline().split())))

print(data[(n-1)//2])