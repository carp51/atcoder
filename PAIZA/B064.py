H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

check = [[1] * W for _ in range(H)]

ans = 0

for i in range(H):
    for j in range(W):
        if check[i][j] == 0:
            continue
        
        x, y = j, i
        visited = [[0] * W for _ in range(H)]
        cnt = 0
        
        while True:
            if visited[y][x] == 0:
                visited[y][x] = 1
                
                if S[y][x] == "U":
                    y -= 1
                elif S[y][x] == "R":
                    x += 1
                elif S[y][x] == "D":
                    y += 1
                elif S[y][x] == "L":
                    x -= 1
                    
                if not 0 <= x < W:
                    break
                
                if not 0 <= y < H:
                    break
            else:
                if cnt == 1:
                    break
                
                if x == j and y == i:
                    ans += 1
                else:
                    break
                    
                x, y = j, i
                visited = [[0] * W for _ in range(H)]
                while True:
                    if visited[y][x] == 0:
                        visited[y][x] = 1
                        check[y][x] = 0
                        
                        if S[y][x] == "U":
                            y -= 1
                        elif S[y][x] == "R":
                            x += 1
                        elif S[y][x] == "D":
                            y += 1
                        elif S[y][x] == "L":
                            x -= 1
                            
                        if not 0 <= x < W:
                            break
                        
                        if not 0 <= y < H:
                            break
                    else:
                        cnt += 1
                        break

print(ans)