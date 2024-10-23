def solution(s):
    answer = True

    if s.startswith(")"):
        return False
    
    n = 0
    for p in s:
        if n < 0:
            return False
        if p == "(":
            n += 1
        elif p == ")":
            n -= 1
    
    if n == 0:
        return True
    else:
        return False