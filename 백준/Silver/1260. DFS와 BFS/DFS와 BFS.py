'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

'''
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

graph = {}
N, M, V = map(int, input().split())

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
        
# 모든 정점 초기화 (간선이 없는 노드도 포함)
for i in range(1, N+1):
    if i not in graph:
        graph[i] = []

print(' '.join(map(str, my_dfs(graph, V))))
print(' '.join(map(str, my_bfs(graph, V))))