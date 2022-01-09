# 셔틀버스 (2018 KAKAO BLIND RECRUITMENT)

# 시간을 문자열 출력 양식대로 변환 후 반환하는 함수
def time_to_string(time):
    return '%02d:%02d' %(time//60, time%60)

def solution(n, t, m, timetable):
    timetable_list=[]
    for time in sorted(timetable):
        tmp=list(map(int, time.split(':')))
        timetable_list.append(tmp[0]*60+tmp[1])
    cur_time=9*60
    while n>1:
        for _ in range(m):
            if timetable_list and timetable_list[0]<=cur_time:
                timetable_list.pop(0)
            else:   # 셔틀버스에 타지 못할 경우
                break
        n-=1
        cur_time+=t   # 현재 시간 업데이트
    # 마지막 버스 (n==1)
    if not timetable_list or len(timetable_list)<m:   # 셔틀 버스 자리가 남는 경우
        return time_to_string(cur_time)
    if timetable_list[m-1]<=cur_time:
        return time_to_string(timetable_list[m-1]-1)
    return time_to_string(cur_time)

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))