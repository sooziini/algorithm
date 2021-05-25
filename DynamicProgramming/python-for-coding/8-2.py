x = int(input())

ret = [0] * 30001

for i in range(2, x+1):
    ret[i] = ret[i - 1] + 1

    if (i % 2 == 0):
        ret[i] = min(ret[i], ret[i // 2] + 1)

    if (i % 3 == 0):
        ret[i] = min(ret[i], ret[i // 3] + 1)

    if (i % 5 == 0):
        ret[i] = min(ret[i], ret[i // 5] + 1)

print(ret[x])