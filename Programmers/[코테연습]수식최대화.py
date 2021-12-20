# 수식 최대화 (2020 KAKAO 인턴십)

from itertools import permutations

# '+', '-', '*' 계산하는 함수
def calc(num1, op, num2):
    if op=='+':
        return str(int(num1)+int(num2))
    elif op=='-':
        return str(int(num1)-int(num2))
    elif op=='*':
        return str(int(num1)*int(num2))

def solution(expression):
    answer=[]
    exp_list, tmp = [], ""
    for e in expression:
        if e.isdigit():
            tmp+=e
        else:
            exp_list.extend([tmp, e])
            tmp=""
    exp_list.append(tmp)    # ['100', '-', '200', '*', '300', '-', '500', '+', '20'] 형태
    for op in permutations(['+', '-', '*'], 3):     # ('+', '-', '*')
        exp=exp_list[:]     # exp_list 깊은 복사
        for o in op:        # '+' / '-' / '*'
            stack=[]
            while len(exp)>0:
                tmp=exp.pop(0)
                if tmp==o:
                    stack.append(calc(stack.pop(), o, exp.pop(0)))
                else:
                    stack.append(tmp)
            exp=stack
        answer.append(abs(int(exp[0])))
    return max(answer)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))