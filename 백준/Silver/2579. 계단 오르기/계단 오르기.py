N = int(input())
scores = [0] + [int(input()) for _ in range(N)]

if N == 0:
    print(0)
elif N == 1:
    print(scores[1])
elif N ==2:
    print(scores[2] + max(scores[0], scores[1]))
else:
    # DP 배열 초기화
    F = [[0] * 2 for _ in range(max(3, N+1))]

    # 시작 상태 정의
    F[0][0] = 0
    F[1][0] = scores[1]
    F[2][0] = scores[2] + F[1][0]
    F[2][1] = scores[2] + F[0][0] # F[0][1]은 존재 X

    for i in range(3, N+1):
        F[i][0] = scores[i] + F[i-1][1]
        F[i][1] = scores[i] + max(F[i-2][0], F[i-2][1])

    print(max(F[N][0], F[N][1]))