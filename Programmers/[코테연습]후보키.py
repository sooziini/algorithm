# 후보키 (2019 KAKAO BLIND RECRUITMENT)

from itertools import combinations

def solution(relation):
    combi_idx = []
    for i in range(1, len(relation[0])+1):
        combi_idx.extend(combinations(range(len(relation[0])), i))
    unique = []
    for c in combi_idx:
        tmp = [tuple([item[i] for i in c]) for item in relation]
        if len(set(tmp))==len(relation):    # 유일성을 만족하는 경우
            chk = True
            for u in unique:
                if set(u).issubset(set(c)): # 최소성을 만족하지 않는 경우
                    chk = False
                    break
            if chk:
                unique.append(c)    # index 조합 append
    return len(unique)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))