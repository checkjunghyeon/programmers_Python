orig = input()
exp = input()

result = []
for i in orig:
    result.append(i)
    if i == exp[-1] and ''.join(result[-len(exp):]) == exp:
        for _ in exp:
            result.pop()

if result:
    print(''.join(result))
else:
    print("FRULA")