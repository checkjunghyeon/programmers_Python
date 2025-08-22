N = int(input())
cost = []
for i in range(N):
    cost.append(list(map(int, input().split())))

if N == 0:
    print(0)
elif N == 1:
    print(min(cost[0]))
else:
    # DP 배열 초기화
    F = [[0] * 3 for _ in range(N + 1)]

    # 시작 상태 정의
    # 0: R, 1: G, 2: B
    F[1][0], F[1][1], F[1][2] = cost[0][0], cost[0][1], cost[0][2]

    # DP 점화식
    for i in range(2, N+1):
        F[i][0] = min(F[i-1][1], F[i-1][2]) + cost[i-1][0]  # RED
        F[i][1] = min(F[i-1][0], F[i-1][2]) + cost[i-1][1]  # GREEN
        F[i][2] = min(F[i-1][0], F[i-1][1]) + cost[i-1][2]  # BLUE

    print(min(F[N][0], F[N][1], F[N][2]))