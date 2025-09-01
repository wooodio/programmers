import math
from collections import defaultdict

def time_cal(time_string):
    hour,second=time_string.split(':')
    return int(hour)*60+int(second)

def solution(fees, records):
    answer=[]
    std_time=fees[0]
    std_fee=fees[1]
    unit_time=fees[2]
    unit_fee=fees[3]
    dic=defaultdict(list)
    
    for record in records:
        time,car_num,status = record.split()
        dic[car_num].append(time_cal(time))
    
    for car in sorted(dic.keys()):
        times= dic[car]
        if len(times)%2==1:
            times.append(23*60+59)
        score=0
        for idx, point in enumerate(times):
            if idx%2==0:
                score-=point
            else:
                score+=point
        if score>=std_time:
            final_score=std_fee+math.ceil((score-std_time)/unit_time)*unit_fee
        else:
            final_score=std_fee
        answer.append(final_score)
    return answer