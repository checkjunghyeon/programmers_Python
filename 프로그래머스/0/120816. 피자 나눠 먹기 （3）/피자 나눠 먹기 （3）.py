def solution(slice, n):
    cnt = 0
    
    while True:
        if max(n, slice * cnt + 1) > n:
            break
        
        cnt += 1

    return cnt