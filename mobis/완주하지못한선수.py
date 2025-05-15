# 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
