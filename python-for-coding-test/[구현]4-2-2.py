n = int(input())
ret = 0

def chk(i):
    if (i % 10 == 3):
        return 1
    elif (i in range(30, 40)):
        return 1
    else:
        return 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if (chk(i) or chk(j) or chk(k)):
                ret += 1

print(ret)