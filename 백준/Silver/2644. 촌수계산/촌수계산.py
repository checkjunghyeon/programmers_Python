from collections import deque

num = int(input())
a, b = map(int, input().split())
m = int(input())

# 양방향 불완전연결 그래프 작성
family = {}
for _ in range(m):
    p1, p2 = map(int, input().split())
    if p1 not in family:
        family[p1] = []
    if p2 not in family:
        family[p2] = []
    family[p1].append(p2)
    family[p2].append(p1)
   

def bfs(graph, start, target):
    visited = set()
    queue = deque()
    queue.append((start, 0))  # (현재 노드, 현재 촌수)

    while queue:
        current, depth = queue.popleft()

        if current == target:
            return depth
        
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):  # 연결 없는 경우도 고려
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))
    
    return -1  # 연결되지 않은 경우

print(bfs(family, a, b))