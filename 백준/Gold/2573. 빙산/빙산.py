from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_ice_groups():
    visited = [[False] * M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                BFS(i, j, visited)
                count += 1
    return count

def melt():
    melt_amount = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if graph[x][y] > 0:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                        melt_amount[x][y] += 1
    for x in range(N):
        for y in range(M):
            graph[x][y] = max(0, graph[x][y] - melt_amount[x][y])

year = 0
while True:
    group_count = count_ice_groups()
    if group_count == 0:
        print(0)
        break
    if group_count >= 2:
        print(year)
        break
    melt()
    year += 1