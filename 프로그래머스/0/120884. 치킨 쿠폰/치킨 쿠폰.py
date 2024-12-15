def solution(chicken):
    answer = 0
    
    _N = 0
    _n = 0
    
    for _ in str(chicken):
        N = chicken // 10
        n = chicken % 10
        chicken = N
        
        _N += N
        _n += n  
    
    answer = _N + (_n // 10)
    print((_n // 10) +(_n % 10))
    
    if (_n // 10) +(_n % 10) == 10:
        answer += 1

    return answer
    # return chicken // 9