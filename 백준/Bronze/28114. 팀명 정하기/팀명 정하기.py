A = list(input().split())
B = list(input().split())
C = list(input().split())

m1 = sorted([str(int(A[1])%100), str(int(B[1])%100), str(int(C[1])%100)])
print(''.join(m1))

m2 = [(int(A[0]), A[2][0]), (int(B[0]), B[2][0]), (int(C[0]), C[2][0])]
m2_sort = sorted(m2, key=lambda x: x[0], reverse=True)
m2_sort_name = [x[1] for x in m2_sort]
print(''.join(m2_sort_name))