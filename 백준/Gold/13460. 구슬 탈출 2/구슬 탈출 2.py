from collections import deque

# 입력 처리
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
 
# '.'은 빈 칸
# '#'은 장애물 또는 벽
# 'O'는 구멍의 위치
# 'R'은 빨간 구슬의 위치
# 'B'는 파란 구슬의 위치

for i in range(N):
    for j in range(M):
        if board[i][j] == 'O':
            gx, gy = i, j
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1    # 이동 거리 
    return x, y, count

def BFS(rx, ry, bx, by):
    queue = deque()
    visited = set()
    queue.append((rx, ry, bx, by, 0))
    visited.add((rx, ry, bx, by))
    
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth >= 10:
            return -1
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i]) 
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            
            if (nbx, nby) == (gx, gy):
                continue
            if (nrx, nry) == (gx, gy):
                return depth + 1 
            
            # 위치 겹치면 조정
            if (nrx, nry) == (nbx, nby):
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1

print(BFS(rx, ry, bx, by))