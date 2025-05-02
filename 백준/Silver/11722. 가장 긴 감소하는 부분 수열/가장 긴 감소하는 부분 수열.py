# 입력값 처리
N = int(input())
seq = list(map(int, input().split()))

# DP 배열 초기화
F = [1] * N  # 각 원소는 자기 자신으로 시작 가능하므로 1로 초기화

# DP식 구현
for i in range(N):
    for j in range(i):
        if seq[i] < seq[j]:
            F[i] = max(F[i], F[j] + 1)

# 결과 출력
print(max(F))