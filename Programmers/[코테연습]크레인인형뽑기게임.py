# 크레인 인형뽑기 게임 (2019 KAKAO 개발자 겨울 인턴십)

def solution(board, moves):
    answer = 0
    r_board = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    basket = []
    for m in moves:
        if r_board[m-1]:
            tmp = r_board[m-1].pop(0)
            if basket and basket[-1] == tmp:
                answer += 2
                basket.pop()
            else:
                basket.append(tmp)
    return answer

# 2
from collections import deque

def solution2(board, moves):
    answer = 0
    r_board, basket = [], []
    for b in list((zip(*board))):
        r_board.append(deque(b))
    for m in moves:
        if r_board[m-1]:
            while not r_board[m-1][0]:
                r_board[m-1].popleft()
            tmp = r_board[m-1].popleft()
            if basket and basket[-1] == tmp:
                answer += 2
                basket.pop()
            else:
                basket.append(tmp)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))