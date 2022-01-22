# 추석 트래픽 (2018 KAKAO BLIND RECRUITMENT)

def get_time_section(lines):
    times=[]
    for line in lines:
        _,_time,_sec=line.rstrip('s').split()
        h,m,s=map(float, _time.split(':'))
        end_time=int((h*3600+m*60+s)*1000)
        times.append((end_time-int(float(_sec)*1000)+1, end_time))
    return times

def solution(lines):
    times=get_time_section(lines)
    answer=1
    for i in range(len(times)):
        section=times[i][1]+999
        cnt=1
        for j in range(i+1, len(times)):
            if times[j][0]<=section:
                cnt+=1
        answer=max(answer, cnt)
    return answer

print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))