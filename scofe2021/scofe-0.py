import math

n, k = map(int, input().split())
data = list(map(int, input().split()))

start = data.index(min(data))   # 가장 작은 값의 인덱스
ret = math.inf                  # 무한대 수 설정

for i in range(k):
    cnt = 1
    # start index를 기준으로 front, back 배열 분할
    front, back = data[:start-i], data[start+k-i:]

    front_cnt = len(front) // (k-1)
    if (len(front)%(k-1)):
        cnt += 1
    back_cnt = len(back) // (k-1)
    if (len(back)%(k-1)):
        cnt += 1
    cnt += front_cnt + back_cnt
    ret = min(cnt, ret)

print(ret)