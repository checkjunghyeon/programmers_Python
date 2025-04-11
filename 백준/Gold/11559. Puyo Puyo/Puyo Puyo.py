from collections import deque

N, M = 12, 6
field = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, visited):
    queue = deque()
    queue.append((x, y))    
    visited[x][y] = True
    group = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and field[x][y] == field[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                group.append((nx, ny))
    return group
                
def block_down():
    for j in range(M):
        for i in range(N-2, -1, -1):  # 아래에서 위로
            if field[i][j] != '.':    # 색상 좌표라면
                r = i                 # i가 곧 x 좌표
                while r+1 < N and field[r+1][j] == '.':
                    field[r+1][j], field[r][j] = field[r][j], field[r+1][j]
                    r += 1
chain = 0
while True:
    bomb_flag = False
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 색상값이 존재 & 방문 X라면 해당 좌표와 같은 색상으로 연결된 그룹 찾기
            if field[i][j] != '.' and not visited[i][j]:
                group = BFS(i, j, visited)
                
                if len(group) >= 4:
                    bomb_flag = True
                    for x, y in group:
                        field[x][y] = '.'

    if not bomb_flag:
        break
        
    block_down()
    chain += 1
    
print(chain)