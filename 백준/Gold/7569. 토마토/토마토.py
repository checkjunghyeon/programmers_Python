from collections import deque

# 최소 일수 구하기 = BFS
# start state : 익은 토마토들의 (x, y) 좌표
# visited : 사용 X
# state : (x, y)
# next state : (x, y)에서 1칸 이동한 ~앞뒤상하좌우~ 좌표
# 종료 조건 : BFS 종료 후 0이 하나라도 있으면 -1 반환 
# 출력 : 그래프의 모든 칸에서의 최대값

# 입력 처리
M, N, H = map(int, input().split())    # 가로, 세로, 높이
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

for z in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[z][x][y] == 1:
                queue.append((x, y, z))
                
while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if boxes[nz][nx][ny] == 0:
                boxes[nz][nx][ny] = boxes[z][x][y] + 1
                queue.append((nx, ny, nz))

days = 0
for row in boxes:
    for col in row:
        for cell in col:
            if cell == 0:
                print(-1)
                exit()
            days = max(days, cell)
print(days - 1)