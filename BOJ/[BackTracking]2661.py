# 좋은 수열 - Back Tracking

import sys

n=int(sys.stdin.readline())

def back_tracking(depth, answer):
    global flag
    if flag:    # 수열을 완성했을 경우 즉시 종료
        return
    if depth>1:
        for i in range(1, depth//2+1):
            if answer[-i:]==answer[-i-i:-i]:
                return
    if depth==n:    # n 길이만큼 수열을 완성했을 경우
        print(answer)
        flag=True
        return
    for d in "123":     # 1, 2, 3 순서대로 탐색
        back_tracking(depth+1, answer+d)

flag=False
back_tracking(0, "")