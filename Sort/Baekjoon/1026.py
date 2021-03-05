
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
result = 0

for _ in range(n):
    result += a_list.pop(a_list.index(min(a_list))) * b_list.pop(b_list.index(max(b_list)))

print(result)