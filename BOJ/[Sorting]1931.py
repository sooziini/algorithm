# 회의실 배정

import sys

n = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 회의 끝나는 시간 오름차순 정렬 후 회의 시작하는 시간 오름차순 정렬
time.sort(key=lambda x:(x[1], x[0]))

endTime = time[0][1]    # 첫번째 끝나는 시간 (최소값)
cnt = 1
for x, y in time[1:]:
    if x >= endTime:    # 다음 회의 시작 시간 >= 끝나는 시간
        cnt += 1
        endTime = y     # 끝나는 시간 재할당
print(cnt)