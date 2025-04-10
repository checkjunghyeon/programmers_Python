from collections import deque

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                queue.append((x, y, z))
                
while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nx, ny, nz))

days = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 0:
                print(-1)
                exit()
            days = max(days, graph[z][y][x])

print(days - 1)  # 처음 익은 날이 1부터 시작했기 때문에 -1