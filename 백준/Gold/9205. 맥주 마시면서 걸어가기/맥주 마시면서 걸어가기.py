from collections import deque


def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) <= 1000

def bfs(coord):
    n = len(coord)
    visited = [False] * n
    
    queue = deque()
    queue.append(0)
    visited[0] = True
    
    while queue:
        current = queue.popleft()
        if current == n - 1:
            return "happy"
        for next in range(n):
            if not visited[next] and manhattan(coord[current], coord[next]):
                visited[next] = True
                queue.append(next)
    return "sad"

tc = int(input())
for _ in range(tc):
    n = int(input())
    coord = [tuple(map(int, input().split())) for _ in range(n+2)]
    print(bfs(coord))
