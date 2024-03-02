from collections import defaultdict


N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(lambda: 0)

for i in range(N):
    r_S = S[i][::-1]
    
    if S[i] <= r_S:
        d[S[i]] = 1
    else:
        d[r_S] = 1


print(len(d))