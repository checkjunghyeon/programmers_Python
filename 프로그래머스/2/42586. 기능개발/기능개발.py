from collections import deque
import math 

def solution(progresses, speeds):
    answer = []

    remainedDays = list(map(lambda x, y: math.ceil((100 - x)/y), progresses, speeds))
    
    _max = remainedDays[0]
    n = 0
    for i, d in enumerate(remainedDays):
        n += 1
        if i == (len(remainedDays)-1):
            answer.append(n)           
        elif _max < remainedDays[i+1]:
            answer.append(n)
            n = 0
            _max = remainedDays[i+1]
        
    return answer