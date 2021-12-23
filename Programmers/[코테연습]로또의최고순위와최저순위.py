# 로또의 최고 순위와 최저 순위 (2021 Dev-Matching)

def solution(lottos, win_nums):
    ok, zero = 0, lottos.count(0)
    for l in lottos:
        if l in win_nums:   # 로또 번호가 일치하는 경우
            ok+=1
    return [7-(ok+zero) if ok+zero!=0 else 6, 7-ok if ok!=0 else 6]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))