N = int(input())
cards = list(map(int, input().split()))
M = int(input())
wanna_know = list(map(int, input().split()))

# 2. collections. Counter 사용
from collections import Counter
cnt = Counter(cards)
print(" ".join(str(cnt[num]) for num in wanna_know))