# 괄호 변환 (2020 KAKAO BLIND RECRUITMENT)

# 균형잡힌 괄호 문자열 u, v로 분리하는 함수
def divide(w):
    open, close = 0, 0
    for i in range(len(w)):
        if w[i]=='(':
            open+=1
        else:
            close+=1
        if open==close:
            return w[:i+1], w[i+1:]

# 올바른 괄호 문자열인지 확인하는 함수
def isCorrect(u):
    stack=[]
    for i in u:
        if i=='(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return True

# 문자열의 괄호 방향을 뒤집는 함수
def change(u):
    tmp=""
    for i in u:
        if i=='(':
            tmp+=')'
        else:
            tmp+='('
    return tmp

def solution(p):
    if not p:       # 빈 문자열일 경우 빈 문자열 return
        return ''
    u, v = divide(p)
    if isCorrect(u):    # u가 올바른 괄호 문자열일 경우
        return u+solution(v)
    else:
        return '('+solution(v)+')'+change(u[1:-1])

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))