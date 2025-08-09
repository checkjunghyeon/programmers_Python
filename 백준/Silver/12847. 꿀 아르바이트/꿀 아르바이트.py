n, m = map(int, input().split())
pays = list(map(int, input().split()))

s = sum(pays[0:m])
max_ = s
for i in range(1, n-m+1):
    s = s - pays[i-1] + pays[i+m-1]
    if max_ < s:
        max_ = s
print(max_)