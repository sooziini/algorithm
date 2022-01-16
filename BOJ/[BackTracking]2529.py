# 부등호 - Back Tracking

import sys

k=int(sys.stdin.readline())
sign=sys.stdin.readline().rstrip().split()

def back_tracking(idx, answer, num_list):
    if idx>0:
        if sign[idx-1]=='<':
            if answer[idx-1]>answer[idx]:
                return -1
        else:
            if answer[idx-1]<answer[idx]:
                return -1
    if idx==k:  # k개의 부등호를 모두 확인했을 경우
        print(answer)
        return 0
    for n in num_list:
        if n not in answer: # 선택한 숫자는 중복이 허용되지 않음
            # 부등호 관계를 만족하는 정수를 완성했을 경우 즉시 종료
            if back_tracking(idx+1, answer+n, num_list)==0:
                return 0

back_tracking(-1, "", "9876543210") # 최대 정수
back_tracking(-1, "", "0123456789") # 최소 정수