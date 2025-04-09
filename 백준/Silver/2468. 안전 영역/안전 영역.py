from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
     
def bfs(x, y, visited, safe_map):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
                 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and safe_map[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    
min_height = min(map(min, graph))
max_height = max(map(max, graph))
max_safe_zone = 0

for h in range(0, max_height + 1):
    safe_map = [[1 if graph[i][j] > h else 0 for j in range(N)] for i in range(N)]
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if safe_map[i][j] == 1 and not visited[i][j]:
                bfs(i, j, visited, safe_map)
                count += 1

    max_safe_zone = max(max_safe_zone, count)

print(max_safe_zone)