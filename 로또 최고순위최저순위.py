def solution(lottos, win_nums):
    #일치수:순위
    #키값이 숫자여도 가능
    score={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    joker= lottos.count(0)
    count = 0
    for lotto in lottos:
        if lotto in win_nums:
            count +=1
    min_score=score[count]
    max_score=score[min(count+joker,6)]
    answer = [max_score,min_score]
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))