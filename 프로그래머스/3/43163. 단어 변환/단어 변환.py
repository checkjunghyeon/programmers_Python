from collections import deque

def is_connect(current, words):
    adj = []
    for word in words:
        diff = 0
        for i, w in enumerate(word):
            if current[i] != w:
                diff += 1
        if diff == 1:
            adj.append(word)        
    return adj

def bfs(start, end, words):
    queue = deque()
    queue.append((start, 0)) # (단어, 변환 횟수)
    visited = []
    visited.append(start)
    
    while queue:
        cur, cnt = queue.popleft()
        
        # 종료 조건
        if cur == end:
            return cnt
        
        for nxt in is_connect(cur, words):    
            if nxt not in visited:
                visited.append(nxt)
                queue.append((nxt, cnt + 1))
    return 0    

def solution(begin, target, words):
    return bfs(begin, target, words)