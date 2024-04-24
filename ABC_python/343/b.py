N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

ans = [[] for i in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            ans[i].append(j + 1)

for i in ans:
    print(*i)