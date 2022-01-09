# 셔틀버스 (2018 KAKAO BLIND RECRUITMENT)

# t분이 더해졌을 때의 시간 계산 후 올바른 양식대로 변환하는 함수
def change_time(time, t):
    time[1]+=t
    if time[1]>59:  # 60분 이상일 경우
        time[0]+=1
    elif time[1]<0: # 0분 미만일 경우
        time[0]-=1
    time[1]%=60
    return time

# 시간을 문자열 출력 양식대로 변환 후 반환하는 함수
def time_to_string(time):
    return '%02d:%02d' %(time[0], time[1])

def solution(n, t, m, timetable):
    timetable_list=sorted(list(map(int, time.split(':'))) for time in timetable)
    cur_time=[9,0]
    while n>1:
        for _ in range(m):
            if timetable_list and timetable_list[0][0]<cur_time[0] or (timetable_list[0][0]==cur_time[0] and timetable_list[0][1]<=cur_time[1]):
                timetable_list.pop(0)
            else:   # 셔틀버스에 타지 못할 경우
                break
        n-=1
        cur_time=change_time(cur_time, t)   # 현재 시간 업데이트
    # 마지막 버스 (n==1)
    if not timetable_list or len(timetable_list)<m:   # 셔틀 버스 자리가 남는 경우
        return time_to_string(cur_time)
    if timetable_list[m-1][0]<cur_time[0] or (timetable_list[m-1][0]==cur_time[0] and timetable_list[m-1][1]<=cur_time[1]):
        return time_to_string(change_time(timetable_list[m-1], -1))
    else:
        return time_to_string(cur_time)

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))