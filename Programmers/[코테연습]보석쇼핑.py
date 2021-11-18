# 보석 쇼핑

# 1. 정확성 O, 효율성 O
from collections import defaultdict

def solution(gems):
    answer = []
    a_x, a_y = 0, 0
    chk_dic = defaultdict(int)      # 보석 각각의 개수
    gems_set_len = len(set(gems))   # 보석 종류 수
    shortest = len(gems)+1          # 최단 길이

    while a_y<len(gems):
        chk_dic[gems[a_y]]+=1
        a_y+=1
        # 딕셔너리에 보석 종류 수만큼 모두 저장했을 경우
        if len(chk_dic)==gems_set_len:
            while a_x<a_y:
                if chk_dic[gems[a_x]]==1:     # 보석이 한개만 남았다면
                    break
                chk_dic[gems[a_x]]-=1
                a_x+=1
            if a_y-a_x<shortest:        # 최단길이 확인
                shortest = a_y-a_x
                answer = [a_x+1, a_y]
    return answer

# 2. 정확성 O, 효율성 X
import copy

def solution2(gems):
    answer_len = len(gems)+1
    a_x, a_y = 1, 1
    gems_set = set(gems)
    for i in range(len(gems)-len(gems_set)+1):
        tmp_set = copy.deepcopy(gems_set)
        tmp_set.remove(gems[i])
        for j in range(i+1,len(gems)):
            if gems[j] not in tmp_set:  # 이미 있는 보석이라면
                continue
            tmp_set.remove(gems[j])
            if len(tmp_set)==0:         # 모든 보석을 포함했을 경우
                if j-i+1 < answer_len:
                    a_x, a_y = i+1, j+1 # 최단길이 확인
                    answer_len = j-i+1
                break
    return [a_x, a_y]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))