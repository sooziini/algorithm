# 튜플 (2019 KAKAO 개발자 겨울 인턴십)

def solution(s):
    answer=[]
    new_s=s.strip('{}').split('},{')
    for n in sorted(new_s, key=len):  # '2','2,1','2,1,3','2,1,3,4' 형태
        item=list(map(int, n.split(',')))
        for i in item:
            if i not in answer: # answer에 없는 숫자일 경우 append
                answer.append(i)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))