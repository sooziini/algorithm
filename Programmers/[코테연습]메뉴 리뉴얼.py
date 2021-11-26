# 메뉴 리뉴얼 (2021 KAKAO BLIND RECRUITMENT)
    
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    for i in range(len(orders)):        # 배열 각 원소 문자열 오름차순 정렬
        orders[i]=''.join(sorted(orders[i]))
    order_max_len=len(max(orders, key=len))     # max 문자열 길이 저장
    for c in course:
        if order_max_len<c:     # 메뉴 구성 불가한 경우
            break
        chk_dict=defaultdict(int)
        for o in orders:
            if len(o)>=c:
                for l in list(combinations(o, c)):
                    chk_dict[''.join(l)]+=1
        max_value=max(list(chk_dict.values()))  # 가장 많이 함께 주문한 단품메뉴 수
        if max_value>=2:    # 최소 2명 이상의 손님이 주문한 메뉴여야 함
            answer+=[k for k, v in chk_dict.items() if v==max_value]
    return sorted(answer)   # 원소 길이 상관없이 오름차순 정렬

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))