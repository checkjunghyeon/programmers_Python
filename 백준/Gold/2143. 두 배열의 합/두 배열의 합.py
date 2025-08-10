import bisect

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 누적합
a_sum, b_sum = [], []

for i in range(n):
    s = A[i]
    a_sum.append(s)
    for j in range(i+1, n):
        s += A[j]
        a_sum.append(s)

for i in range(m):
    s = B[i]
    b_sum.append(s)
    for j in range(i+1, m):
        s += B[j]
        b_sum.append(s)

# 이분 탐색
a_sum.sort()
b_sum.sort()

answer = 0 
for i in range(len(a_sum)):
    left = bisect.bisect_left(b_sum, T-a_sum[i])
    right = bisect.bisect_right(b_sum, T-a_sum[i])
    answer += right-left
print(answer)