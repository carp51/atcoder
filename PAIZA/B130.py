N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(3)]

for i in range(N):
    for j in range(10):
        S[i].append("#")

for i in range(10):
    S.append(["#"] * (M + 10))

for i in range(N):
    for j in range(M):
        for _ in range(4):
            flag = True
            T = [list(x) for x in zip(*T[::-1])]
            
            for h in range(3):
                for w in range(3):
                    if T[h][w] == "#":
                        if S[i + h][j + w] == "#":
                            flag = False
                            
            if flag:
                print("Yes")
                exit(0)
                
print("No")