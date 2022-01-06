# 가장 큰 수 - Sorting

def solution(numbers):
    num_list=list(map(str, numbers))
    num_list.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(num_list)))  # [0, 0] -> '0' return 해야 함

# 시간 초과
from itertools import permutations

def solution2(numbers):
    answer=[]
    for p in permutations(list(map(str, numbers)), len(numbers)):
        answer.append(''.join(p))
    return str(int(max(answer)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0]))