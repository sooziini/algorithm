x = int(input())

ret = [0] * 30001

for i in range(2, x+1):
    # 첫번째 경우: x - 1
    ret[i] = ret[i - 1] + 1

    # 두번째 경우: x % 2 == 0
    if (i % 2 == 0):
        ret[i] = min(ret[i], ret[i // 2] + 1)

    # 세번째 경우: x % 3 == 0
    if (i % 3 == 0):
        ret[i] = min(ret[i], ret[i // 3] + 1)

    # 네번째 경우: x % 5 == 0
    if (i % 5 == 0):
        ret[i] = min(ret[i], ret[i // 5] + 1)

print(ret[x])