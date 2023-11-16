H, W = map(int, input().split())

A = [list(map(int, input().split())) for i in range(H)]

ans = [["."] * W for i in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] != 0:
            ans[i][j] = chr(A[i][j] + 64)
            
for i in ans:
    i = map(str, i)
    print("".join(i))