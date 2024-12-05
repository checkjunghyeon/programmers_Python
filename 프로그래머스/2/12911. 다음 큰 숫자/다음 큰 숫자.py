def solution(n):
    a = get_ones(n)
    N = n + 1
    while True:
        if a == get_ones(N):
            break
        N += 1
    return N

def get_ones(n):
    cnt = 1
    while True:
        q = n//2
        r = n%2
        if r == 1:
            cnt += 1
        n = q
        if q == 1:
            break
    return cnt