# 정수 삼각형 - DP

def solution(triangle):
    dp = [[0]*n for n in range(1, len(triangle)+1)]
    dp[0][0]=triangle[0][0]
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):   # 마지막줄 전까지
            dp[i+1][j]=max(dp[i][j]+triangle[i+1][j], dp[i+1][j])   # 바로 아래
            dp[i+1][j+1]=max(dp[i][j]+triangle[i+1][j+1], dp[i+1][j+1]) # 대각선 아래
    return max(dp[len(triangle)-1])     # 마지막줄 dp값 중 max 리턴

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))