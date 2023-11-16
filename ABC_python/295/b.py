R, C = map(int, input().split())
B = [list(input()) for i in range(R)]

for i in range(R):
    for j in range(C):
        for r in range(R):
            for c in range(C):
                if not (B[i][j] == "." or B[i][j] == "#"): 
                    if abs(i - r) + abs(j - c) <= int(B[i][j]):
                        if B[r][c] != "#":
                            if B[r][c] != ".":
                                continue
                        B[r][c] = "."
                        
for i in range(R):
    for j in range(C):
        if not (B[i][j] == "." or B[i][j] == "#"): 
            B[i][j] = "."
            
for i in B:
    print("".join(i))