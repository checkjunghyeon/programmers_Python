from collections import deque

def bfs(x, y, maps):
    queue = deque()
    queue.append((x, y))
    
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)] # 방문 X면 0, 방문 시엔 이동 횟수 기록
    visited[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == (n-1, m-1):
            return visited[n-1][m-1]
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return -1

def solution(maps):
    return bfs(0, 0, maps)
    