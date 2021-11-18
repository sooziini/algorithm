data = input()
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) + 1
ret = 0
possible = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

for i in possible:
    tmpx = x + i[0]
    tmpy = y + i[1]
    if (tmpx < 1 or tmpx > 8 or tmpy < 1 or tmpy > 8):
        continue
    ret += 1

print(ret)