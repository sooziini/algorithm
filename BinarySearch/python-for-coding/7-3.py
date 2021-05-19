import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

# 현재 잘린 떡의 길이 구하는 함수
def calc(data, mid):
    sum = 0
    for i in data:
        if (mid < i):
            sum += i - mid
    return sum

def binary_search(target, start, end):
    arr = []

    while (start <= end):
        mid = (start+end) // 2

        sum = calc(data, mid)

        # 잘린 떡의 길이가 요청한 떡의 길이와 같을 경우
        if (sum == target):
            return mid
        # 잘린 떡의 길이가 요청한 떡의 길이보다 작을 경우 왼쪽 탐색
        elif (sum < target):
            end = mid - 1
            arr.append((mid, sum))
        # 잘린 떡의 길이가 요청한 떡의 길이보다 클 경우 오른쪽 탐색
        else:
            start = mid + 1
            arr.append((mid, sum))

    # 탐색 완료 후
    arr.sort(key=lambda x:x[1])
    cur = arr[0][1]
    for t in arr:
        if (target < t[1]):
            return t[0]
    
data.sort()
ret = binary_search(m, 0, data[n-1])
print(ret)