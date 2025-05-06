# 타겟 넘버 - BFS/DFS

answer = 0

def dfs(numbers, target, sum, idx):
    global answer
    if len(numbers) == idx:
        if target == sum:
            answer += 1
        return
    
    dfs(numbers, target, sum + numbers[idx], idx + 1)
    dfs(numbers, target, sum - numbers[idx], idx + 1)

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
