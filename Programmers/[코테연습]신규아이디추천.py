# 신규 아이디 추천 (2021 KAKAO BLIND RECRUITMENT)

import re

def solution(new_id):
    # ^: 괄호 안의 문자를 제외한 모든 문자
    # 1단계, 2단계: 소문자로 변환, 소문자/숫자/-/_/. 제외한 문자 모두 제거
    answer = re.sub("[^-_.a-z0-9]", "", new_id.lower())
    # 3단계: '.' 문자가 2번 이상 연속된 부분을 1개로 변환
    if answer:      
        tmp = answer[0]
        chk = False
        if tmp=='.':
            chk = True  # '.' 문자가 나온 경우 True
        for i in range(1, len(answer)):
            if answer[i]!='.':
                tmp+=answer[i]
                chk=False
            elif not chk:       # 첫 '.' 문자일 경우
                tmp+=answer[i]
                chk=True
    # 4단계: 맨 앞, 맨 뒤 "." 문자 제거
    answer = tmp.strip('.')
    # 5단계, 6단계: 빈 문자열일 경우 'a' 대입, 15자리까지 슬라이싱 + 마지막 '.' 문자 제거
    answer = 'a' if not answer else answer[:15].rstrip('.')
    # 7단계: 길이가 2 이하일 경우 마지막 문자를 길이 3이 될 때까지 반복
    if len(answer)<=2:
        answer+=answer[-1]*(3-len(answer))
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))