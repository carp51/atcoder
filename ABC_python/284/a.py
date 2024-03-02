N = int(input())
S = [input() for _ in range(N)]

for i in range(N-1, -1, -1):
    print(S[i])