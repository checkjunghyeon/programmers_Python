from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    
    while queue:
        current = queue.popleft()
        
        if not visited[current]:
            visited[current] = True
            queue.extend(graph.get(current, [])) # 불완전연결그래프 고려

def solution(n, computers):
    # 그래프 생성
    graph = {}

    for i in range(n):
        for j in range(n):
            # 그래프 연결 시, 자기 자신 제외
            if i == j:
                continue
            # 연결된 노드 리스트 추가
            if computers[i][j] == 1:
                if i not in graph:
                    graph[i] = []
                graph[i].append(j)
    
    visited = [False] * n
    cnt = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(graph, i, visited)
            cnt += 1
            
    return cnt