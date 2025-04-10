from collections import deque

R, C = map(int, input().strip().split())
maze = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fire_time = [[-1] * C for _ in range(R)]
jihoon_time = [[-1] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

fqueue = deque()
jqueue = deque()
                
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            fqueue.append((i, j))
            fire_time[i][j] = 0
        if maze[i][j] == 'J':
            jqueue.append((i, j))
            visited[i][j] = True
            jihoon_time[i][j] = 0
            if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                print(1)
                exit()
           
while fqueue:
    x, y = fqueue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and fire_time[nx][ny] == -1 and maze[nx][ny] != '#':
            fire_time[nx][ny] = fire_time[x][y] + 1
            fqueue.append((nx, ny))


while jqueue:
    x, y = jqueue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != '#' and not visited[nx][ny]:
            jihoon_time[nx][ny] = jihoon_time[x][y] + 1
            jqueue.append((nx, ny))
            visited[nx][ny] = True
            
escape_time = float('inf')
for i in range(R):
    for j in range(C):
        if visited[i][j]:  # 방문한 좌표라면
            if i == 0 or i == R-1 or j == 0 or j == C-1:  # 가장자리
                if fire_time[i][j] == -1 or jihoon_time[i][j] < fire_time[i][j]:
                    escape_time = min(escape_time, jihoon_time[i][j] + 1)


if escape_time == float('inf'):
    print("IMPOSSIBLE")
else:
    print(escape_time)
 