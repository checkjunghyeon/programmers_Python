sentence = [list(input()) for _ in range(5)]

# max_len = len(sentence[0])
max_len = max(len(r) for r in sentence)
sub = [[''] * max_len for _ in range(5)]

for i in range(5):
    for j in range(len(sentence[i])):
        sub[i][j] = sentence[i][j]

for j in range(max_len):
    for i in range(5):
        print(sub[i][j], end="")