import math
def solution(progresses, speeds):
    answer = []

    daysToComplete = list(map(lambda x, y: math.ceil((100 - x)/y), progresses, speeds))
    
    currentMaxDay = daysToComplete[0]
    n = 0
    for i in range(len(daysToComplete)):
        n += 1
        if i == len(daysToComplete)-1 or currentMaxDay < daysToComplete[i+1]:
            answer.append(n)
            n = 0
            if i != len(daysToComplete) - 1:
                currentMaxDay = daysToComplete[i+1]
        
    return answer