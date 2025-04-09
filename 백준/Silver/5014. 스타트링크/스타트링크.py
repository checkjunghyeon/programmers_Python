from collections import deque

F, S, G, U, D = map(int, input().split())

def BFS(start, target):
    queue = deque()
    queue.append((start, 0))    # 시작 버튼 누른 횟수는 0번
    visited = [False] * F    # idx: 0 ~ (F-1)
    dy = [U, -D]    # 위로 U층만큼, 아래로 D층만큼
    
    while queue:
        current, count = queue.popleft()
        if current == target:
            return count
        
        for i in range(2):
            _next = current + dy[i]
            if 1 <= _next < F+1 and not visited[_next-1]:
                visited[_next-1] = True
                queue.append((_next, count+1))
    return -1

result = BFS(S, G)
print("use the stairs" if result == -1 else result)