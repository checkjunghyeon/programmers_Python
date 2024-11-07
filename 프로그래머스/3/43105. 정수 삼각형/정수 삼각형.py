def solution(triangle):
    level = len(triangle) # 5
       
    for i in range(level-2, -1, -1): # 3, 2, 1, 0
        for j in range(i, -1, -1): # 4-0 / 3-0 / ... / 0
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
            
    return triangle[0][0]