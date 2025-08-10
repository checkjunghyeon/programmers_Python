# 2차원 배열 다루기
# 행렬 덧셈

# 두 행렬 A, B를 더하는 프로그램 작성
N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
# C = [[0] * M for _ in range(N)]

# # 행렬 덧셈 => 같은 자리에 있는 친구들 끼리 묶기
# for i in range(N):
#     for j in range(M):
#         C[i][j] = A[i][j] + B[i][j]
#     print(*C[i])

# 크기가 같은 배열이라면 zip을 활용하기
for ra, rb in zip(A, B):
    print(*[x + y for x, y in zip(ra, rb)])