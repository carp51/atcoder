def check(h, w):
    D = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    
    cnt = 0
    
    while True:
        for d in D:
            dx = w
            dy = h
            
            dx += d[0] * cnt
            dy += d[1] * cnt
            
            if not (0 <= dx < W):
                return cnt
            
            if not (0 <= dy < H):
                return cnt
            
            if C[dy][dx] == ".":
                return cnt
            
        cnt += 1
            
from collections import defaultdict

check_n = defaultdict(int)

H, W = map(int, input().split())

C = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        check_n[check(i, j) - 1] += 1
        
ans = []

for i in range(1, min(H, W) + 1):
    ans.append(check_n[i])
    
print(*ans)