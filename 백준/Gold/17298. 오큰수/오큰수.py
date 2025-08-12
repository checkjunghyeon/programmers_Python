from collections import deque

N = int(input())
A = list(map(int, input().split()))

stack = []
answer = [-1 for _ in range(N)]

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)