# 문자열 압축 (2020 KAKAO BLIND RECRUITMENT)

def solution(s):
    if len(s)==1:       # s의 길이가 1일 경우 최소 길이 1 return
        return 1
    answer = []         # 압축하여 표현한 문자열의 길이를 담는 배열
    for i in range(1, len(s)//2+1):
        cur, cnt, ret = s[:i], 1, ""
        for j in range(i, len(s), i):
            if cur==s[j:j+i]:   # 현재 문자열과 다음 문자열이 같을 경우 cnt+=1
                cnt+=1
            else:       # 현재 문자열과 다음 문자열이 다를 경우
                if cnt!=1:
                    ret+=str(cnt)
                ret+=cur
                cur, cnt = s[j:j+i], 1
        if cnt!=1:      # 배열의 마지막 번째
            ret+=str(cnt)
        ret+=cur
        answer.append(len(ret))
    return min(answer)
    
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))