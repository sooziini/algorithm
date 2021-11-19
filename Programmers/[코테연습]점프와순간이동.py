# 점프와 순간 이동 (Summer/Winter Coding ~2018)

# solution2 리팩토링
def solution(n):
    ans = 1         # 0->1 무조건 점프해야 함
    while 2<n:
        ans+=n%2    # 홀수일 경우 카운트+1
        n//=2
    return ans

def solution2(n):
    ans = 1         # 0->1 무조건 점프해야 함
    while 2<n:
        if n%2!=0:  # 홀수일 경우 짝수로 변경
            ans+=1
        n//=2
    return ans

print(solution(5))
print(solution(6))
print(solution(5000))