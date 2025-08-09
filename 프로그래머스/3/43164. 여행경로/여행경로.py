from collections import deque

def dfs(start, graph, tickets):
    stack = []
    stack.append(start)
    visited = []
    
    while stack:
        cur = stack[-1]
        if graph.get(cur, []):
            stack.append(graph[cur].pop())
        else:
            visited.append(stack.pop())
    return visited[::-1]

def solution(tickets):
    graph = {}
    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    
    for a in graph:
        graph[a].sort(reverse=True)
    
    return dfs("ICN", graph, tickets)