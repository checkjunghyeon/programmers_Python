def solution(n, s):
    answer = []
    if s//n == 0:
        return [-1]
    
    while n >= 1:
        rem = s//n
        answer.append(rem)
        s = s-rem
        n = n-1
    return answer