N = int(input())

ans = []
S = [input() for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        
        ans.append(S[i] + S[j])
        
ans = list(set(ans))
print(len(ans))
    