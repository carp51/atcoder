N = int(input())
S = input()

ans = []

for i in range(N):
    for j in range(2):
        ans.append(S[i])
        
print("".join(ans))