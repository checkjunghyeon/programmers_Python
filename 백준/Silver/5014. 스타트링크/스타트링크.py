from collections import deque

F, S, G, U, D = map(int, input().split())

def BFS(start, target):
    queue = deque()
    queue.append((start, 0))    # 시작 버튼 누른 횟수는 0번
    visited = [False] * (F+1)   # idx 0은 사용 X
    
    while queue:
        current, count = queue.popleft()
        if current == target:
            return count
        
        for i in [U, -D]:
            _next = current + i
            if 1 <= _next < F+1 and not visited[_next]:
                visited[_next] = True
                queue.append((_next, count+1))
    return -1

result = BFS(S, G)
print("use the stairs" if result == -1 else result)