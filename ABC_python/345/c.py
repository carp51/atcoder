from collections import defaultdict
S = input()
d = defaultdict(lambda: 0) 

for i in range(len(S)):
    d[S[i]] += 1
    
ans = 0

for i in range(len(S)):
    d[S[i]] -= 1
    ans += len(S) - i - d[S[i]] - 1
    
if len(list(set(S))) == len(S):
    print(ans)
else:
    print(ans + 1)