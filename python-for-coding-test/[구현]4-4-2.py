n, m = map(int, input().split())
x, y, direc = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
map_data[x][y] = 2
ret = 1

# 방향을 왼쪽으로 바꾸는 함수
def direcChange():
    global direc 
    direc -= 1
    if (direc == -1):
        direc = 3

chk = 0
while (True):
    direcChange()

    tmpx = x + move[direc][0]
    tmpy = y + move[direc][1]

    # map_data의 값이 0이고 방문하지 않았을 경우
    if (map_data[tmpx][tmpy] == 0):
        x, y = tmpx, tmpy
        map_data[x][y] = 2
        ret += 1
        chk = 0
        continue
    else:
        chk += 1

    # 네 방향 모두 방문한 곳이거나 막혀있는 경우
    if (chk == 4):
        tmpx = x - move[direc][0]
        tmpy = y - move[direc][1]
        if (map_data[tmpx][tmpy] == 2):
            x, y = tmpx, tmpy
            chk = 0
        else:
            break

print(ret)