from itertools import combinations
def solution(number):
    answer = 0
    three = combinations(number, 3)
    
    for t in three:
        if sum(t) == 0:
            answer += 1
        
    return answer