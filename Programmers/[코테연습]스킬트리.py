# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:  # "BACDE"
        cur_idx = 0     # skill index
        for s in sk:    # "B"
            if s in skill:      # skill에 해당되는지 확인
                if skill[cur_idx]!=s:   # 선행스킬 안함
                    break
                cur_idx+=1
                if cur_idx==len(skill)-1:   # "CBADF"
                    answer+=1
                    break
            if s==sk[-1]:   # "AECB" "CBA"
                answer+=1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))