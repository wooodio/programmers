def solution(N, stages):
    
    stay_stages = [0 for _ in range(N+1)]
    for stage in stages:
        stay_stages[stage-1] += 1
    print(stay_stages)
    
    pass_stages= [sum(stay_stages[n:]) for n in range(len(stay_stages))]
    print(pass_stages)

    fail_rates= [stay/passing for stay,passing in zip(stay_stages,pass_stages)][:-1]
    print(fail_rates)
    
    
    answer = [idx+1 for idx,rate in sorted(enumerate(fail_rates), key=lambda x: x[1], reverse=True)]
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
#[3,4,2,1,5]



