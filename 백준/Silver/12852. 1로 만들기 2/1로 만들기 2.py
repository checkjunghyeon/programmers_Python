N = int(input())

# DP 배열 초기화
F = [0] * max(4, N+1) # 1~N, 최소 길이 4

# 시작 상태 정의(bottom-up)
F[1], F[2], F[3] = 0, 1, 1
list = [N]

# DP식 구현
for i in range(4, N+1):
    if i % 3 == 0 and i % 2 == 0:
        F[i] = min(F[i//3], F[i//2], F[i-1]) + 1
    elif i % 3 == 0:
        F[i] = min(F[i//3], F[i-1]) + 1
    elif i % 2 == 0:
        F[i] = min(F[i//2], F[i-1]) + 1
    else:
        F[i] = F[i-1] + 1

orig = N
while orig > 1:
    candidates = []
    if orig % 3 == 0:
        candidates.append((F[orig//3], orig//3))
    if orig % 2 == 0:
        candidates.append((F[orig//2], orig//2))
    candidates.append((F[orig-1], orig-1))

    minimum, nxt = min(candidates)
    orig = nxt
    list.append(orig)


print(F[N])
print(*list)
