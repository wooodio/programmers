import numpy as np

def solution(n):
    answer = np.zeros((n, n), dtype=int)
    shell = 0  
    start = 1  

    while n > 0:
        if n == 1:
            answer[shell, shell] = start
            break

        answer[shell, shell:n-1+shell] = np.arange(start, start + (n-1))
        start += (n-1)
        answer[shell:shell+n-1, n-1+shell] = np.arange(start, start + (n-1))
        start += (n-1)
        answer[n-1+shell, shell+1:n+shell] = np.arange(start + n-2, start - 1, -1)
        start += (n-1)
        answer[shell+1:n+shell, shell] = np.arange(start + n-2, start - 1, -1)
        start += (n-1)
        
        n -= 2
        shell += 1

    return answer
        
print(solution(3))       
        
        
        
        


