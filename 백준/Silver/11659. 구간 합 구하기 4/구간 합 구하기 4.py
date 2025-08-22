N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = []

F = [0] * (N + 1)
F[0], F[1] = 0, nums[0]
for k in range(2, N+1):
    F[k] = F[k-1] + nums[k-1]

for _ in range(M):
    i, j = map(int, input().split())
    result.append(str(F[j] - F[i-1]))

print("\n".join(result))