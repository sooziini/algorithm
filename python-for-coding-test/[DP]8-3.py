n = int(input())
data = list(map(int, input().split()))

ret = [0] * 100

ret[0] = data[0]
ret[1] = max(data[0], data[1])

# 현재 위치 기준 바로 옆 식량창고에 갈 수 없으므로
# [i-1] or [i-2] + 현재
for i in range(2, n):
    ret[i] = max(ret[i - 1], ret[i - 2] + data[i])

print(ret[n - 1])