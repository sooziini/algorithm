# 표 편집 (2021 KAKAO 채용연계형 인턴십)

linked_list = {}

def set_k_u_d(num, k, ver):
    for _ in range(num):
        k = linked_list[k][ver]
    return k

def set_k_c(prev, next, n):
    global linked_list
    if next == n:
        linked_list[prev][1] = next
        return prev
    else:
        if prev != -1:
            linked_list[prev][1] = next
        linked_list[next][0] = prev
        return next

def set_back(prev, next, num, n):
    global linked_list
    if next != n:
        linked_list[next][0] = num
    if prev != -1:
        linked_list[prev][1] = num

def solution(n, k, cmd):
    global linked_list
    linked_list = {x:[x-1, x+1] for x in range(n)}
    answer = ['O' for _ in range(n)]
    deleted = []
    for c in cmd:
        if len(c) > 1:
            c, x = c.split()
        if c == 'U':
            k = set_k_u_d(int(x), k, 0)
        elif c == 'D':
            k = set_k_u_d(int(x), k, 1)
        elif c == 'C':
            prev, next = linked_list[k]
            deleted.append((prev, next, k))
            answer[k] = 'X'
            k = set_k_c(prev, next, n)
        elif c == 'Z':
            prev, next, num = deleted.pop()
            answer[num] = 'O'
            set_back(prev, next, num, n)
    return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))