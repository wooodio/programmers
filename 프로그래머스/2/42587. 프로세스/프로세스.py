
def solution(priorities, location):
    len_p=len(priorities)
    dic={}
    cnt=0
    
    for i in range(len_p):
        dic[i]=priorities[i]
    process=list(range(len_p))
    
    while(location in list(dic.keys())):
        pop_process=process.pop(0)
        if dic[pop_process]>=max(list(dic.values())):
            del dic[pop_process]
            cnt+=1
        else:
            process.append(pop_process)
        
    return cnt