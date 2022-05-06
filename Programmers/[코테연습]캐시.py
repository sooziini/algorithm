# 캐시 (2018 KAKAO BLIND RECRUITMENT)

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize < 1:
        answer += len(cities) * 5
    else:
        q = deque([], maxlen=cacheSize)
        for city in cities:
            c = city.lower()
            if c in q:
                q.remove(c)
                answer += 1
            else:
                answer += 5
            q.append(c)
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))