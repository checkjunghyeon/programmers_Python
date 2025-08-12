N = int(input())
words = [input().strip() for _ in range(N)]  # strip 사용법 알기

# 정렬 
words_sorted = sorted(set(words), key=lambda x: (len(x), x))
print("\n".join(words_sorted))