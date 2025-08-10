# 1차원 배열 다루기
# X보다 작은 수

# 문제: 수열 A에서 X보다 작은 수를 모두 출력
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 완전 탐색
# for a in A:
#     if a < X:
#         print(a, end=' ')

# 간단 버전
print(*[a for a in A if a < X])