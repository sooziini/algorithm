n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# sorted 내림차순 정렬
arr.sort(reverse=True)

for i in arr:
    print(i, end=" ")