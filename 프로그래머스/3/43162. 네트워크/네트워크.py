from collections import deque

def bfs(start, visited, computers, n):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        cur = queue.popleft()
        for nxt in range(n):
            if cur != nxt and computers[cur][nxt] == 1 and not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers, n)
            cnt += 1
            
    return cnt