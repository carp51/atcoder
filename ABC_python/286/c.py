N, A, B = map(int, input().split())
S = input()

ans = 10 ** 20

for i in range(N - 1):
    check = S[1: len(S)] + S[:1]
    

    tmp = 0

    for j in range(N // 2):
        if S[j] != S[N - j - 1]:
            tmp += 1

    ans = min(ans, tmp * B + i * A)
    S = check

print(ans)