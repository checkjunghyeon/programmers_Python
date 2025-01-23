import math
def solution(n,a,b):
    answer = 0

    while True:
        if abs(a-b) < 1:
            break
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        
    return answer