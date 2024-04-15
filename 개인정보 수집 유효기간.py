def solution(today, terms, privacies):
    answer=[]
    today_val = cal(today)                   
    terms_dic = {term.split(' ')[0]:int(term.split(' ')[1]) for term in terms}
    for idx, privacy in enumerate(privacies):
        start = privacy.split(' ')[0]
        start_val = cal(start)
        due_val = start_val + terms_dic[privacy.split(' ')[1]]*28
        if today_val>=due_val:
            answer.append(idx+1)    
    return answer

def cal(date):
    date_split= list(map(int,date.split('.')))                
    date_val = (date_split[0]-2000)*12*28 + date_split[1]*28 + date_split[2]
    return date_val

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))