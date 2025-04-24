N = int(input())

F = [0] * max(3, (N + 1))  # DP 배열 초기화
F[0], F[1], F[2] = 0, 1, 2  # 시작 상태 정의

# Bottom-up Method
if N >= 3:
    for i in range(3, N+1):
        F[i] = F[i-1] + F[i-2]
print(F[N] % 10007)