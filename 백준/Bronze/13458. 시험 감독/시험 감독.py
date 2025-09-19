N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

sum = N
for a in A:
    remain = a - B
    if remain > 0:
        sum += ((remain + C -1) // C)

print(sum)