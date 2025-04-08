from collections import deque

MAX = 100001
visited = [-1] * MAX # N에서부터 해당 위치까지 도달하는데 걸리는 시간 배열

def bfs(start, target):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.popleft()

        if current == target:
            return visited[current]

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

N, K = map(int, input().split())
print(bfs(N, K))
