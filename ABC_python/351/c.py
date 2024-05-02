N = int(input())
A = list(map(int, input().split()))

S = []

for i in range(N):
    S.append(A[i])
    
    while len(S) > 1:
        if S[-1] != S[-2]:
            break
        else:
            tmp = S[-1]
            S.pop()
            S.pop()
            S.append(tmp + 1)
            
print(len(S))