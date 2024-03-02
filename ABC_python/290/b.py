N, K = map(int, input().split())
S = list(input())

for i in range(N):
    if S[i] == "o":
        if K > 0:
            K -= 1
        else:
            S[i] = "x"
            
print("".join(S))