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
    flag = False
    for i in range(n):
        if (x + i >= n or y + i >= n or flag):
            break
        # 현재 좌표의 오른쪽, 아래쪽, 대각선 확인
        if (chk(x+i, y) and chk(x, y+i) and chk(x+i, y+i)):
            # 해당 정사각형이 3x3 이상일 경우
            if (i > 1):
                j = 1
                while (j < i):
                    if (chk(x+i-j, y+i) and chk(x+i, y+i-j)):
                        total += 1
                        ret[i] += 1
                        j += 1
                    else:
                        flag = True
                        break
            # 해당 정사각형이 1x1 or 2x2일 경우
            else:
                total += 1
                ret[i] += 1
        else:
            break

for i in range(n):
    for j in range(n):
        if (arr[i][j] == 1):
            calc(n, i, j)

# 결과 출력
print("total: %d" %total)
for i in range(n):
    if (ret[i] == 0):
        continue
    print("size[%d]: %d" %(i+1, ret[i]))