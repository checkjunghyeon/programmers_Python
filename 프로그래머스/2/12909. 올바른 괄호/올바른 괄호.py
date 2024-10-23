def solution(s):
    answer = True

    n = 0
    for p in s:
        if p == "(":
            n += 1
        elif p == ")":
            n -= 1
            
        # 닫는 괄호가 먼저 나오는 경우
        if n < 0:
            return False
    
    if n == 0:
        return True
    else:
        return False