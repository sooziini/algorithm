# 오픈채팅방 (2019 KAKAO BLIND RECRUITMENT)

def solution(record):
    answer = []
    user_dict={}
    for r in record:
        _r = r.split()
        if len(_r)>2:   # Enter, Change
            user_dict[_r[1]]=_r[2]
    for r in record:
        _r = r.split()
        if _r[0]=="Enter":
            answer.append(user_dict[_r[1]]+"님이 들어왔습니다.")
        if _r[0]=="Leave":
            answer.append(user_dict[_r[1]]+"님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))