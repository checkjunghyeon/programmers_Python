tc = int(input())
for _ in range(tc):
    N = int(input())
    F = [0] * max(4, N + 1)
    F[1], F[2], F[3] = 1, 2, 4

    for n in range(4, N+1):
        F[n] = sum([F[i] for i in range(n-3, n)])

    print(F[N])