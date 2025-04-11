from collections import deque

N, M, K = map(int, input().split())
fireballs = deque()
for _ in range(M):
    fireballs.append(list(map(int, input().split())))

# 0~7
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # 파이어볼 이동
    grid = [[[] for _ in range(N)] for _ in range(N)]
    
    # 파이어볼이 존재하는 좌표마다
    while fireballs:
        x, y, m, s, d = fireballs.popleft()
        nx = (x + dx[d]*s) % N    # ∵ 행렬 시계 방향 순회 이동
        ny = (y + dy[d]*s) % N
        grid[nx][ny].append([m, s, d])    # 이동 후 위치마다 질량, 속력, 방향 저장    
    
    # 파이어볼 합치고 나누기
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) == 0:    # 빈 좌표
                continue
            elif len(grid[i][j]) == 1:    # 파이어볼 1개만 존재
                fireballs.append([i, j] + grid[i][j][0])    # [x, y, m, s, d]
            else:
                total_m = sum(f[0] for f in grid[i][j])
                total_s = sum(f[1] for f in grid[i][j])
                count = len(grid[i][j])
                dirs = [f[2] % 2 for f in grid[i][j]]
                
                new_m = total_m // 5
                if new_m == 0:
                    continue
                new_s = total_s // count
                if all(d == dirs[0] for d in dirs):
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]
                    
                for nd in new_dirs:    # 4개 추가
                    fireballs.append([i, j, new_m, new_s, nd])

# 질량 합 출력
print(sum(f[2] for f in fireballs))