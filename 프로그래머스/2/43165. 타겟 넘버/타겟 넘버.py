from collections import deque

def solution(numbers, target):
    cnt = 0
    queue = deque()
    queue.append((0, 0)) # (현재 합, 방문할 인덱스)
    
    while queue:
        total, idx = queue.popleft()
        
        # 종료 조건: 모든 숫자를 다 센 경우
        if idx == len(numbers):
            if total == target:
                cnt += 1
            continue

        # +와 -의 경우 각각 queue에 추가
        queue.append((total + numbers[idx], idx+1)),
        queue.append((total - numbers[idx], idx+1))
    
    return cnt