n = int(input())
data = list(map(int, input()))
ret = 0

def dfs(x):
    if (x >= n-2):
        global ret
        ret += 1
        return
    if (data[x+1] == 0):
        dfs(x+2)
    else:
        dfs(x+1)
        if (data[x+2] != 0):
            dfs(x+2)
dfs(0)
print(ret)