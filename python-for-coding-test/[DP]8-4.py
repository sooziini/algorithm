n = int(input())

ret = [0] * 1001

ret[1] = 1      # 2 x 1 = 1가지
ret[2] = 3      # (2 x 1)*2 + (1 x 2)*2 + (2 x 2)*1 = 3가지

# [i-1]의 경우 (2 x 1) = 1가지
# [i-2]의 경우 (1 x 2)*2 + (2 x 2)*1 = 2가지
for i in range(3, n+1):
    ret[i] = (ret[i-1] + ret[i-2]*2) % 796796

print(ret[n])