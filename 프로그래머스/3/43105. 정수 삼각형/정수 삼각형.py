def solution(triangle):
    level = len(triangle)
    # DP 배열 초기화(2차원 배열)
    F = [[0] * level for _ in range(level)]
    
    # DP 초기값 정의
    F[0][0] = triangle[0][0]
    
    # DP식 반복
    for i in range(1, level):
        for j in range(0, i+1):
            left = F[i-1][j] + triangle[i][j]
            right = F[i-1][j-1] + triangle[i][j]
            F[i][j] = max(left, right)
    
    return max(F[-1])