# 주차 요금 계산 (2022 KAKAO BLIND RECRUITMENT)

import math

def change_time(time):
    hh,mm=time.split(':')
    return int(hh)*60+int(mm)

def is_out(cars, car_num, out_time, in_time):
    if car_num not in cars:
        cars[car_num]=0
    cars[car_num]+=change_time(out_time)-in_time
    return cars

def calc_fee(time, fees):
    if time<=fees[0]:
        return fees[1]
    return fees[1]+math.ceil((time-fees[0])/fees[2])*fees[3]

def solution(fees, records):
    answer = []
    cars,time_logs={},{}    # cars={차 번호:주차 누적 시간}, time_logs={차 번호:입차한 시간}
    for record in records:
        time,car_num,status=record.split()
        if status=="IN":
            time_logs[car_num]=change_time(time)
        elif status=="OUT":
            cars=is_out(cars, car_num, time, time_logs[car_num])
            time_logs.pop(car_num)
    for car_num, in_time in time_logs.items():
        cars=is_out(cars, car_num, "23:59", in_time)
    for _, total_time in sorted(cars.items()):
        answer.append(calc_fee(total_time, fees))
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))