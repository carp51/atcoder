from sortedcontainers import SortedSet, SortedList, SortedDict

N, K = map(int, input().split())
P = list(map(int, input().split()))

Q = [-1] * N
for i in range(N):
  p = P[i] - 1
  Q[p] = i


S = SortedSet()

ans = 10 ** 20

for i in range(N):
    if len(S) < K:
        S.add(Q[i])
    else:
        min_num = S[0]
        max_num = S[K - 1]
        ans = min(ans, max_num - min_num)
        
        S.discard(Q[i - K])
        S.add(Q[i])
        
min_num = S[0]
max_num = S[K - 1]
ans = min(ans, max_num - min_num)
        
print(ans)