def solution(info, n, m):
    F = [[[False] * m for _ in range(n)] for _ in range(len(info) + 1)]
    F[0][0][0] = True
    
    for i, (info_a, info_b) in enumerate(info):
        for A in range(n):
            for B in range(m):
                if F[i][A][B]:
                    na = A + info_a
                    nb = B + info_b
                    
                    # i+1번째 물건을 A가 훔친 경우
                    if na < n:
                        F[i+1][na][B] = True
                    # i+1번째 물건을 B가 훔친 경우
                    if nb < m:
                        F[i+1][A][nb] = True
                
    for a in range(n):
        for b in range(m):
            if F[len(info)][a][b]:
                return a
            
    return -1 