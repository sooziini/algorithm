# 호텔 방 배정 (2019 KAKAO 개발자 겨울 인턴십)

# 정확성O / 효율성O
# 반복문 사용
def solution(k, room_number):
    answer=[]
    room_dict={}    # {현재 방 번호:다음 빈방 번호}
    for n in room_number:
        r=n
        visited=[r]
        while r in room_dict:   # 이미 배정된 방일 경우
            r=room_dict[r]
            visited.append(r)
        answer.append(r)
        for i in visited:
            room_dict[i]=r+1
    return answer

# 정확성O / 효율성O
# 재귀 사용
import sys
sys.setrecursionlimit(10**6)

def find_room(n, room_dict):
    if n not in room_dict:
        room_dict[n]=n+1
        return n
    empty=find_room(room_dict[n], room_dict)
    room_dict[n]=empty+1    # n의 부모 노드 값을 배정된 방 번호+1로 업데이트
    return empty

def solution(k, room_number):
    answer=[]
    room_dict={}    # {현재 방 번호:다음 빈방 번호}
    for n in room_number:
        answer.append(find_room(n, room_dict))
    return answer

# 정확성O / 효율성X
def solution2(k, room_number):
    answer = []
    for n in room_number:
        if n not in answer:
            answer.append(n)
        else:   # 이미 배정된 방일 경우
            for i in range(n+1, k+1):
                if i not in answer:
                    answer.append(i)
                    break
    return answer

print(solution(10, [1,3,4,1,3,1]))