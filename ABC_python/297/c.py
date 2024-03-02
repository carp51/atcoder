H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            continue
        elif S[h][w] == "T":
            if w == W - 1:
                continue
            else:
                if S[h][w + 1] == "T":
                    S[h][w] = "P"
                    S[h][w + 1] = "C"
                    
for i in S:
    print("".join(i))