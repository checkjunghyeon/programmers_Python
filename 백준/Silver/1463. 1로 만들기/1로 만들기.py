N = int(input())

# DP 배열 초기화
F = [0] * (max(4, N+2))  # 최소 크기 4 이상 확보

# 시작 상태 정의
F[1], F[2], F[3] = 0, 1, 1

# DP식 구현
for n in range(4, N+1):
    # 2의 배수면서 3의 배수인 경우
    if n % 3 == 0 and n % 2 == 0:
        F[n] = 1 + min(F[n-1], F[n//2], F[n//3])
    # 3의 배수인 경우
    elif n % 3 == 0:
        F[n] = 1 + min(F[n-1], F[n//3])
    # 2의 배수인 경우
    elif n % 2 == 0:
        F[n] = 1 + min(F[n-1], F[n//2])
    # 나머지 경우
    else:
        F[n] = 1 + F[n-1]

# 값 반환
print(F[N])