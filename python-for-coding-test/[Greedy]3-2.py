n, m, k = map(int, input().split())
data = list(map(int, input().split()))
ret = 0
chk = 0

data.sort(reverse=True)
max_num = data[0]       # data에서 가장 큰 수
max_num_2 = data[1]     # data에서 두번째로 큰 수

for i in range(m):
    if (chk < k):
        ret += max_num
        chk += 1
    else:
        ret += max_num_2
        chk = 0

print(ret)

    
