N = int(input())
nums = sorted(list(map(int, input().split())))

good_cnt = 0

for i in range(N):
    target = nums[i]
    left, right = 0, N-1

    while left < right:
        # i번째 값 제외
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        # 서로 다른 두 개의 수를 더해
        s = nums[left] + nums[right]
        if s == target:
            good_cnt += 1
            break
        elif s < target:
            left += 1
        else:
            right -= 1
print(good_cnt)