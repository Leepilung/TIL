def solution(progresses, speeds):
    answer = []
    timegab = []
    count = 1
    for i,j in zip(progresses,speeds):    
        timegab.append(-((i - 100) // j))
        while len(timegab) >= 2 :
            if timegab[0] < timegab[1]:
                timegab.pop(0)
                answer.append(count)
                count = 1
            
            elif timegab[0] >= timegab[1]:
                timegab.pop(1)
                count +=1
    if len(timegab) == 1:
        answer.append(count)
    
    return answer