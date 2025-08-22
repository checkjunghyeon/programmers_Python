N = int(input())
scores = [int(input()) for _ in range(N)]

# 0 <= N < 3인 경우 예외 처리
if N == 0:
    print(0)
elif N == 1:
    print(scores[0])
elif N == 2:
    print(scores[0] + scores[1])
else:
    # DP 배열 초기화
    # F[a][b] : a 계단까지 (b+1)칸 이동
    F = [[0] * 2 for _ in range(N+1)]  # (N+1) x 2
    
    # 시작 상태 정의
    F[0][0] = 0
    F[1][0] = scores[0]
    F[2][0] = scores[1] + F[1][0]
    F[2][1] = scores[1] + F[0][0]

    for i in range(2, N):
        F[i+1][0] = scores[i] + F[i][1]  # 1칸 연속
        F[i+1][1] = scores[i] + max(F[i-1][0], F[i-1][1])  # 2칸 점프

    print(max(F[N][0], F[N][1]))