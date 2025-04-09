# 방문 순서(X) 개수 카운팅(O)
# 최단 거리 = BFS

from collections import deque

# 입력 처리
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    
    # 상하좌우 이동 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:    # (0,0)은 방문처리가 안 돼도 괜찮음!
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[N-1][M-1]

print(BFS(0, 0))
