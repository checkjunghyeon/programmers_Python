N, K =  map(int, input().split())
temp = list(map(int, input().split()))

s = sum(temp[0:K])
max_ = s
for i in range(1, N-K+1):
    s = s - temp[i-1] + temp[i+K-1]
    if s > max_:
        max_ = s
print(max_)

