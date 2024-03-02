S = input()

for i in range(len(S)):
    if S[i].isupper():
        print(i + 1)
        break