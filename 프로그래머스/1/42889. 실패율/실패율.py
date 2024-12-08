def solution(N, stages):
    # answer = list(range(N))
    answer = []
    reach = [0] * N
    fail = [0] * N
    
    # for n in range(1, N+1):
    #     for s in stages:
    #         if s >= n:
    #             if s == n:
    #                 fail[n-1] += 1
    #             reach[n-1] += 1
    
    for s in stages:
        if s <= N:
            fail[s - 1] += 1
        for i in range(min(s, N)):
            reach[i] += 1
            
    failure = list(map(safe_division, fail, reach))

    for _f in sorted(failure, reverse=True):
        k = failure.index(_f)
        answer.append(k + 1)
        failure[k] = -1
        
    return answer

def safe_division(x, y):
    return x / y if y != 0 else 0