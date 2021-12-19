# 전화번호 목록 - Sorting & String

import sys

t = int(sys.stdin.readline())
answer=[]
for tc in range(t):
    n = int(sys.stdin.readline())
    num_list=sorted([sys.stdin.readline().rstrip() for _ in range(n)])  # num_list 정렬
    for i in range(len(num_list)-1):
        if num_list[i+1].startswith(num_list[i]):   # i+1 문자열이 i 문자열로 시작하는지 확인
            answer.append("NO")
            break
    if len(answer)!=tc+1:   # 한 번호가 다른 번호의 접두어인 경우가 없을 경우
        answer.append("YES")
for a in answer:
    print(a)