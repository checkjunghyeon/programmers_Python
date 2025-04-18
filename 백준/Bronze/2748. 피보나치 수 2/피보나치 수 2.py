n = int(input())

# DP 배열을 0으로 초기화
F = [0] * (n + 1)

# 시작 상태 정의
F[0], F[1] = 0, 1

# Fn = Fn-1 + Fn-2 (n ≥ 2) 구현
for i in range(2, n + 1):
    F[i] = F[i-1] + F[i-2]

print(F[-1])