# 격자이동

answer = 0

def dfs(x, y, n, arr, sum):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    global answer
    if x == n - 1 and y == n - 1:
        answer = max(answer, sum + arr[x][y])
        return
    dfs(x + 1, y, n, arr, sum + arr[x][y])
    dfs(x, y + 1, n, arr, sum + arr[x][y])

def solution(n, arr):
    dfs(0, 0, n, arr, 0)
    return answer

print(solution(5, [[1, 8, 2, 5, 5], [6, 3, 3, 6, 5], [1, 10, 5, 5, 5], [5, 4, 5, 2, 7], [6, 9, 6, 8, 5]]))
