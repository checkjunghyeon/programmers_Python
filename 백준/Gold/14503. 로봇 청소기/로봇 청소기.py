N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 0 -> 청소되지 않은 빈 칸 / 1 -> 벽(이동 불가능)
graph = [list(map(int, input().split())) for _ in range(N)]
count = 0

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(graph, x, y):
    global count
    count += 1
    graph[x][y] = -1
   
while True:
    if graph[r][c] == 0:    # 현재 위치 청소 여부 확인
        clean(graph, r, c)
         
    moved = False    
    for _ in range(4):
        d = (d+3) % 4    # 90도 반시계 방향 
        nx, ny = r + dx[d], c + dy[d]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            r, c = nx, ny
            moved = True
            break
        else:
            continue
                
    if not moved:
        back = (d+2) % 4    # 180도 반대 방향 
        nx, ny = r + dx[back], c + dy[back]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:
            r, c = nx, ny
        else:
            print(count)
            break
