N = int(input())
target = [int(input()) for _ in range(N)]

cur_num = 1
ops = []    # +/-
stack = []

# 목표 수열 순서대로
# 현재 칸의 숫자와 비교해서
# 작거나 같을 때까지 stack에 push
# 마지막 숫자를 stack에서 pop
# 마지막 숫자를 pop할 수 없는 경우(stack이 비어있거나, stack의 마지막 숫자가 목표 숫자가 아닌 경우) - NO 출력

for x in target:
    while cur_num <= x:
        stack.append(cur_num)
        ops.append("+")
        cur_num += 1

    if not stack or stack[-1] != x:
        print("NO")
        break

    stack.pop()
    ops.append("-")

# for-else
# for문을 끝까지 돌고 나면 실행
else:
    print("\n".join(ops))


