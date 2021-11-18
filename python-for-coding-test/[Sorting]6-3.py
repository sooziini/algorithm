n = int(input())
arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

# 두번째 원소를 기준으로 정렬
ret = sorted(arr, key=lambda x: x[1])

for i in ret:
    print(i[0], end=" ")