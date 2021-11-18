n, m = map(int, input().split())
min_num = 0
max_num = 0

for i in range(n):
    tmp = list(map(int, input().split()))   # 한 줄씩 입력 받기
    min_num = min(tmp)                      # 최솟값 저장
    
    if (max_num < min_num):
        max_num = min_num                   # 최솟값 중 최댓값 저장

print(max_num)
