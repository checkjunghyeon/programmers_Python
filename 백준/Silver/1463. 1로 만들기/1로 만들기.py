N = int(input())

F = [0] * max(4, N+1) # 1~N, 최소 길이 4
F[1], F[2], F[3] = 0, 1, 1

for i in range(4, N+1):
    if i % 3 == 0 and i % 2 == 0:
        F[i] = min(F[i//3], F[i//2], F[i-1]) + 1
    elif i % 3 == 0:
        F[i] = min(F[i//3], F[i-1]) + 1
    elif i % 2 == 0:
        F[i] = min(F[i//2], F[i-1]) + 1
    else:
        F[i] = F[i-1] + 1

print(F[N])