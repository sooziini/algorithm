# 기능개발 - Queue

from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque([-((p - 100) // s) for p, s in zip(progresses, speeds)])
    cnt = 1
    cur = q.popleft()
    while q:
        day = q.popleft()
        if day <= cur:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            cur = day
    answer.append(cnt)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))