N = int(input())
S = [list(input()) for i in range(N)]

length = -1

for i in range(N):
    length = max(length, i + len(S[i]))

l = [[""] * N for i in range(length)]

for i in range(N):
    for j in range(len(S[i])):
        l[j + i][N - i - 1] = S[i][j]
        
for i in l:
    print(" ".join(i))