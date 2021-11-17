# 카드게임 - 구현

import sys

numList = []   # 숫자만 담을 배열
colorSet = set()   # 모두 같은 색인지 확인할 집합
for _ in range(5):
    color, num = sys.stdin.readline().split()
    colorSet.add(color)
    numList.append(int(num))
numList.sort()

# 카드 5장이 모두 같은 색인지 확인
colorChk = True if len(colorSet)==1 else False

cur = numList[0]    # 현재 숫자
cnt = 1             # 숫자가 연속되는 횟수
cntList = []        # 연속되는 횟수 저장하는 배열
numConti = 0
for i, num in enumerate(numList[1:]):   # index 0부터 시작
    if cur == num:  # 숫자가 같은 경우
        cnt += 1
        if i==3:    # 마지막 숫자
            cntList.append((cnt, cur))
        continue
    if cnt != 1:
        cntList.append((cnt, cur))
        cnt = 1
    if cur+1 == num:    # 연속된 숫자인 경우
        numConti += 1
    cur = num

numContiChk = True if numConti==4 else False    # 연속된 숫자인지 확인
cntList.sort(key=lambda x:(x[0], x[1]), reverse=True)

ret = 0
if colorChk and numContiChk:
    ret = numList[4]+900
elif len(cntList) and cntList[0][0]==4:
    ret = cntList[0][1]+800
elif len(cntList)==2 and cntList[0][0]==3 and cntList[1][0]==2:
    ret = (cntList[0][1]*10)+cntList[1][1]+700
elif colorChk:
    ret = numList[4]+600
elif numContiChk:
    ret = numList[4]+500
elif len(cntList) and cntList[0][0]==3:
    ret = cntList[0][1]+400
elif len(cntList)==2 and cntList[0][0]==2 and cntList[1][0]==2:
    ret = (cntList[0][1]*10)+cntList[1][1]+300
elif len(cntList) and cntList[0][0]==2:
    ret = cntList[0][1]+200
else:
    ret = numList[4]+100
print(ret)