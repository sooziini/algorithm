# 로또 - Mathematics

import sys
from itertools import combinations

lotto=[]
while True:
    _lotto=list(sys.stdin.readline().split())
    if _lotto.pop(0)=='0':
        break
    lotto.append(_lotto)

for l in lotto:
    for i in list(combinations(l, 6)):
        print(' '.join(i))
    print()