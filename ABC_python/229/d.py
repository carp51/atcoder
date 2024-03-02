from bisect import bisect_right

S = input()
K = int(input())

N = len(S)

cs = [0]

for i in range(N):
    if S[i] == ".":
        cs.append(cs[-1] + 1)
    else:
        cs.append(cs[-1])

ans = -10

for i in range(1, N + 1):
    target = cs[i] + K
    if S[i - 1] == ".":
        ans = max(ans, bisect_right(cs, target - 1) - i)
    else:
        ans = max(ans, bisect_right(cs, target) - i)

print(ans)