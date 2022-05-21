# 압축 (2018 KAKAO BLIND RECRUITMENT)

def solution(msg):
    answer = []
    alpha_dict = {chr(ord('A')+i):i+1 for i in range(0, 26)}
    w, c = 0, 1
    while True:
        if c == len(msg):
            answer.append(alpha_dict[msg[w:c]])
            break
        if msg[w:c+1] not in alpha_dict:
            answer.append(alpha_dict[msg[w:c]])
            alpha_dict[msg[w:c+1]] = len(alpha_dict) + 1
            w = c
        c += 1
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))