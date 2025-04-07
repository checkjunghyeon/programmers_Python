def my_dfs(graph, start_node):
    stack, visited = [], []  # 방문할 노드를 담을 Stack & 방문 여부 구분을 위한 List 생성

    stack.append(start_node)  # 탐색 시작노드를 Queue에 삽입  

    while stack:  # Stack이 비어있을 때까지 (= 방문할 노드가 없을 때까지)
        cur_node = stack.pop()  # 현재 방문할 노드 꺼내기
        
        if cur_node not in visited:	  # 꺼낸 노드가 방문하지 않은 노드라면
            visited.append(cur_node)  # 방문했음을 기록하기 위해 List에 추가
            stack.extend(reversed(graph[cur_node]))  # 인접 노드를 Stack에 반대 순서로 삽입(LIFO)
    return visited

def my_bfs(graph, start_node):    
    queue, visited = [], []  # 방문할 노드를 담을 Queue & 방문 여부 구분을 위한 List 생성

    queue.append(start_node)  # 탐색 시작노드를 Queue에 삽입  

    while queue:  # Queue가 비어있을 때까지 (= 방문할 노드가 없을 때까지)
        cur_node = queue.pop(0)  # 현재 방문할 노드 꺼내기

        if cur_node not in visited:	  # 꺼낸 노드가 방문하지 않은 노드라면
            visited.append(cur_node)  # 방문했음을 기록하기 위해 List에 추가
            queue.extend(graph[cur_node])  # 인접 노드를 Queue에 순서대로 삽입
    return visited

N, M, V = map(int, input().split())

graph = {}
for n in range(N):
    graph[n] = []
    
for _ in range(M):
    a, b = map(int, input().split())
    
    if a in graph.keys():
        graph[a].append(b)
    else: 
        graph[a] = [b]

    if b in graph.keys():
        graph[b].append(a)
    else: 
        graph[b] = [a]
        
for node in graph:
    graph[node].sort()

print(' '.join(map(str, my_dfs(graph, V))))
print(' '.join(map(str, my_bfs(graph, V))))