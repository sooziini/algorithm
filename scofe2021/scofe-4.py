point = list(map(float, input().split()))
n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]
prefer = [list(input()) for _ in range(n)]

# 출력을 위해 콘텐츠, 선호도, 콘텐츠 해당 인덱스 모두 저장
def newArr(arr):
    global point
    global prefer

    new = []
    for a in arr:
        i, j = a[0], a[1]
        p = prefer[i][j]
        new.append((p, point[ord(p) - ord('A')], i, j))
    new.sort(key=lambda x:x[1], reverse=True)
    return new

# 결과를 출력하는 함수
def retPrint(arr):
    for a in arr:
        for i in range(4):
            print(a[i], end=' ')
        print()

# 'Y'와 'O'에 해당하는 콘텐츠의 인덱스를 저장하는 리스트
yarr = []
oarr = []
for i in range(n):
    for j in range(m):
        # 유저의 콘텐츠 열람 정보 확인 후 인덱스 따로 저장
        if (data[i][j] == 'Y'):
            yarr.append((i, j))
        if (data[i][j] == 'O'):
            oarr.append((i, j))

ynew = newArr(yarr)
onew = newArr(oarr)

retPrint(ynew)
retPrint(onew)