import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().rstrip().split()))

# 현재 존재하는 부품 정렬
data.sort()

def binary_search(arr, target, start, end):
    while (start <= end):
        mid = (start+end) // 2

        # target 값을 찾았을 경우 mid index return
        if (arr[mid] == target):
            return mid
        # target 값이 중간값보다 작을 경우 왼쪽 탐색
        elif (target < arr[mid]):
            end = mid - 1
        # target 값이 중간값보다 클 경우 오른쪽 탐색
        else:
            start = mid + 1
    return None

for i in range(m):
    ret = binary_search(data, find[i], 0, n-1)
    if (ret == None):
        print('no', end=' ')
    else:
        print('yes', end=' ')