# 숫자 문자열과 영단어 (2021 KAKAO 채용연계형 인턴십)

def solution(s):
    answer, tmp = "", ""
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in s:
        if '0'<=i<='9':
            answer+=i
        else:
            tmp+=i
        if tmp and tmp in num_list:
            answer+=str(num_list.index(tmp))
            tmp=""
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))