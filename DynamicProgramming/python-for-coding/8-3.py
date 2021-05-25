n = int(input())
data = list(map(int, input().split()))

ret = [0] * 100

ret[0] = data[0]
ret[1] = max(data[0], data[1])
for i in range(2, n):
    ret[i] = max(ret[i - 1], ret[i - 2] + data[i])

print(ret[n - 1])