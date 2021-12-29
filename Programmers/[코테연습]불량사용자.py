# 불량 사용자 (2019 KAKAO 개발자 겨울 인턴십)

from itertools import permutations

# 현재 튜플이 불량 아이디 목록과 같은지 확인하는 함수
def chk(p_tuple, banned_id):
    for idx, p in enumerate(p_tuple):
        if len(p)!=len(banned_id[idx]):     # 길이가 다를 경우 같은 아이디가 아님
            return False
        for j in range(len(p)):
            if banned_id[idx][j]=='*':
                continue
            elif p[j]!=banned_id[idx][j]:
                return False
    return True

def solution(user_id, banned_id):
    chk_list=[]
    for p_tuple in permutations(user_id, len(banned_id)):
        if chk(p_tuple, banned_id): # 현재 튜플이 불량 아이디 목록과 같을 경우
            tmp=''.join(sorted(p_tuple))
            if tmp not in chk_list:     # 아이디의 목록이 동일한지(set) 체크
                chk_list.append(tmp)
    return len(chk_list)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))