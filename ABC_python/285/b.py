N = int(input())
S = input()

for i in range(N - 1):
    ans = 0
    for j in range(N - i - 1):
        if S[j] != S[j + i + 1]:
            ans += 1
        else:
            break

    print(ans)