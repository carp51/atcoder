S = input()

ans = 0

n = len(S) - 1

for i in range(len(S)):
    ans += 26 ** (n) * (ord(S[i]) - 64)
    n -= 1

print(ans)

