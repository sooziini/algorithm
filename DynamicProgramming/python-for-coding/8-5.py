n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))

ret = [10001] * (m+1)

for i in data:
    cnt = 1
    print(i)
    for j in range(1, m+1):
        if (ret[j] % i == 0):
            ret[j] = min(cnt, ret[j])
            cnt += 1

print(ret[m])