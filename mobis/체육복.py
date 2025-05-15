# 체육복
# Greedy

def solution(n, lost, reserve):
    # 여벌 체육복 가진 학생이 도난당한 경우 처리
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
    return n - len(lost_set)

print(solution(5, [2, 4], [1, 3, 5]))
