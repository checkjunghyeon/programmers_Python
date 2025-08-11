N = int(input())
cards = list(map(int, input().split()))
M = int(input())
wanna_know = list(map(int, input().split()))

# 1. 카운터 내장함수 사용
# O(N * M) - 시간 초과
# for num in wanna_know:
#    print(cards.count(num), end=" ") # O(N)

# 2. collections. Counter 사용
# O(N+M) - 통과
from collections import Counter
cnt = Counter(cards)
print(" ".join(str(cnt[num]) for num in wanna_know))

# 3. 해시(Dictionary)
# 3-1.
# freq = {}
# for c in cards:
#     freq[c] = freq.get(c, 0) + 1
# 
# print(' '.join(str(freq.get(num, 0)) for num in wanna_know))

# 3-2.
# from collections import defaultdict

# freq = defaultdict(int)
# for c in cards:
#     freq[c] = freq[c] + 1
# 
# print(" ".join(str(freq[num]) for num in wanna_know))

# 4. bisect
# O(N log N) + O(M log N)
# import bisect
# answer = []
# cards.sort()
# for num in wanna_know:
#     l = bisect.bisect_left(cards, num)
#     r = bisect.bisect_right(cards, num)
#     answer.append(str(r-l))
# print(' '.join(answer))
