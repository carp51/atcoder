N = int(input())
S = list(input())

flag = True

for i in range(N):
    if S[i] == '"':
        if flag:
            flag = False
        else:
            flag = True

    if S[i] == ',':
        if flag:
            S[i] = '.'

print("".join(S))