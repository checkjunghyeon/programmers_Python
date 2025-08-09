from collections import defaultdict

def dfs(start, graph, tickets):
    stack = []
    stack.append(start)
    
    visited = []
    
    while stack:
        cur = stack[-1] # stack의 맨 위(top)
        if graph[cur]:  # 현재 노드의 인접 노드가 존재한다면 
            stack.append(graph[cur].pop()) # stack(도착지가 하나밖에 없어서 단순 append)
        else:
            visited.append(stack.pop())
    return visited[::-1]

def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    
    for a in graph:
        graph[a].sort(reverse=True)
    
    return dfs("ICN", graph, tickets)