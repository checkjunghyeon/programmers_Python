from itertools import combinations
from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)] # 0: 빈칸, 1: 벽, 2: 바이러스
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(board, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    queue.append((nx, ny))

zero_idx = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero_idx.append((i, j))

max_area = 0
for combi in combinations(zero_idx, 3):
    tmp = [row[:] for row in lab]

    # 벽 세우기
    tmp[combi[0][0]][combi[0][1]] = 1
    tmp[combi[1][0]][combi[1][1]] = 1
    tmp[combi[2][0]][combi[2][1]] = 1

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                bfs(tmp, i, j)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1

    if max_area < cnt:
        max_area = cnt

print(max_area)