from collections import deque

N = int(input())

# 카드 순서대로 넣기
queue = deque(list(range(1, N+1)))

# 카드 버리는 과정 반복
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])