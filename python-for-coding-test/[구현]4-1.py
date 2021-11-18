n = int(input())
map_data = input().split()
x, y = 1, 1

def chk(x, y, n):
    if (x < 1 or x > n or y < 1 or y > n):
        return 0
    return 1

for i in map_data:
    if (i == 'R'):
        if(chk(x, y + 1, n)):
            y += 1
    elif (i == 'L'):
        if(chk(x, y - 1, n)):
            y -= 1
    elif (i == 'U'):
        if(chk(x - 1, y, n)):
            x -= 1
    elif (i == 'D'):
        if(chk(x + 1, y, n)):
            x += 1
    else:
        continue

print(x, y)