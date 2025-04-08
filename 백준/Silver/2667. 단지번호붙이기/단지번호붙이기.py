from collections import deque

N = int(input())
graph = []

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input())))
    
def bfs(x, y):
    # 4. 단지 내 집 세기 (DFS or BFS 사용)
    # DFS 또는 BFS를 써서 해당 위치와 연결된 모든 집을 방문
    # 방문할 때마다 카운트 1씩 증가
    # 연결된 모든 집 방문 완료되면 → 카운트를 단지 리스트에 저장
    queue = deque()
    queue.append((x, y))
    graph[x][y] = -1  # 시작 지점 방문 표시
    count = 1         # 시작 지점도 집이므로 1부터 시작
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]       
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue
                
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                queue.append((nx, ny))
                count += 1
    return count

answer = []
for row in range(N):
    for col in range(N):
        # 3. 방문 체크와 단지 세기
        # graph 값을 수정하여 방문 여부 체크
        # 전체 graph를 순회하면서, 값이 1이면 → 단지 시작
        if graph[row][col] == 1:
            answer.append(bfs(row, col))

print(len(answer))
for a in sorted(answer):
    print(a)