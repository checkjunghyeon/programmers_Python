# 1차원 배열 다루기
# 10807번) 개수 세기

# 정수 v가 몇 개인지 세는 프로그램
N = int(input())
nums = list(map(int, input().split()))
v = int(input())

print(nums.count(v))

# 1. 완전 탐색
# cnt = 0
# for n in nums:
#     if n == v:
#         cnt += 1
# print(cnt)

# 2. 이분 탐색
# import bisect

# nums.sort()
# l = bisect.bisect_left(nums, v)
# r = bisect.bisect_right(nums, v)
# answer = r - l
# print(answer)

# 3. 카운터
# from collections import Counter
# print(Counter(nums)[v])