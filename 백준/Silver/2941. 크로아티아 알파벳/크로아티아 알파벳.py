croatia_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

i, count = 0, 0
while i < len(word):
    if word[i:i+3] in croatia_words:
        count += 1
        i += 3
    elif word[i:i+2] in croatia_words:
        count += 1
        i += 2
    else:
        count += 1
        i += 1

print(count)
