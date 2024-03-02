N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for i in range(1, N):
    for j in range(i+1, N+1):
        flag = True
        for k in range(M):
            if S[i-1][k] == 'o' or S[j-1][k] == 'o':
                continue
            else:
                flag = False
                break
        if flag:
            ans += 1

print(ans)