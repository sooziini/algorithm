# 키패드 누르기 (2020 KAKAO 인턴십)

def solution(numbers, hand):
    answer=''
    cur_left, cur_right = [3, 0], [3, 2]
    for n in numbers:
        if n==1 or n==4 or n==7:
            answer+='L'
            cur_left=[n//3, 0]
        elif n==3 or n==6 or n==9:
            answer+='R'
            cur_right=[n//3-1, 2]
        else:
            tmp = [n//3, 1] if n!=0 else [3, 1]
            left_dist=abs(cur_left[0]-tmp[0])+abs(cur_left[1]-tmp[1])
            right_dist=abs(cur_right[0]-tmp[0])+abs(cur_right[1]-tmp[1])
            if left_dist==right_dist:   # 거리가 같을 경우
                if hand=="left":
                    answer+='L'
                    cur_left=tmp
                else:
                    answer+='R'
                    cur_right=tmp
            elif left_dist>right_dist:  # 오른손으로 누를 경우
                answer+='R'
                cur_right=tmp
            else:       # 왼손으로 누를 경우
                answer+='L'
                cur_left=tmp
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))