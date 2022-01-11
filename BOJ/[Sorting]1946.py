# 신입 사원 - Sorting

import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    employee=sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)])
    min_grade=employee[0][1]    # 서류 1위인 지원자의 면접 순위
    cnt=1   # 서류 1위인 지원자는 무조건 신입사원에 해당
    for i in range(1, n):
        if employee[i][1]<min_grade:
            min_grade=employee[i][1]
            cnt+=1
    print(cnt)