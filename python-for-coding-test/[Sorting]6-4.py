n, k = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)

for i in range(k):
    if (i >= n):
        break
    if (arrA[i] < arrB[i]):
        arrA[i], arrB[i] = arrB[i], arrA[i]

# 배열 A의 모든 원소의 합 구하기
ret = 0
for i in arrA:
    ret += i

print(ret)