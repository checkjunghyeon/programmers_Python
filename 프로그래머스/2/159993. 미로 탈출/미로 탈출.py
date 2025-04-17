from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])  # 직사각형 모양 지도
    maze = [list(maps[row]) for row in range(N)]

    for i in range(N):
        for j in range(M):
            if maze[i][j] == "E":
                ex, ey = i, j
            elif maze[i][j] == "L":
                lx, ly = i, j
            elif maze[i][j] == "S":
                sx, sy = i, j

    fromStoL = bfs(maze, (sx, sy), (lx, ly), N, M)
    if fromStoL == -1:
        return -1
    
    fromLtoE = bfs(maze, (lx, ly), (ex, ey), N, M)
    if fromLtoE == -1:
        return -1
    
    return fromStoL + fromLtoE

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, start, target, N, M):
    queue = deque()
    queue.append(start)  # (x, y) 형식 저장

    visited = [[-1] * M for _ in range(N)]  # 이동 시간 저장
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
                    
        if (x, y) == target:
            return visited[x][y]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return -1