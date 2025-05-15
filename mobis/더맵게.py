# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    hq = scoville[:]
    heapq.heapify(hq)
    while hq[0] < K:
        if len(hq) < 2:
            return -1
        new_num = heapq.heappop(hq) + (heapq.heappop(hq) * 2)
        heapq.heappush(hq, new_num)
        answer += 1
    return answer

# 시간 초과 (sorted 사용)
def solution2(scoville, K):
    answer = 0
    data = sorted(scoville)
    while data[0] < K:
        if len(data) < 2:
            return -1
        new_num = data[0] + (data[1] * 2)
        data = sorted(data[2:] + [new_num])
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
