n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
total = 0
ret = [0 for i in range(n)]

# 현재 좌표에 해당하는 값이 1인지 확인하는 함수
def chk(x, y):
    global arr
    if (arr[x][y] == 1):
        return True
    return False

# 현재 좌표 기준으로 가능한 정사각형 수 구하는 함수
def calc(n, x, y):
    global total
    global ret
    for i in range(n):
        if (x + i >= n or y + i >= n):
            break
        # 현재 좌표의 오른쪽, 아래쪽, 대각선 확인
        if (chk(x+i, y) and chk(x, y+i) and chk(x+i, y+i)):
            total += 1
            ret[i] += 1

for i in range(n):
    for j in range(n):
        if (arr[i][j] == 1):
            calc(n, i, j)

# 결과 출력
print("total: %d" %total)
for i in range(n):
    if (ret[i] == 0):
        continue
    print("size[%d]: %d" %(i, ret[i]))