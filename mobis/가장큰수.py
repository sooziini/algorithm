# 가장 큰 수

def solution(numbers):
    num_list = list(map(str, numbers))
    sorted_list = sorted(num_list, key=lambda x: x * 3, reverse=True)
    return '0' if sorted_list[0] == '0' else ''.join(sorted_list)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
