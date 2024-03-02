from collections import defaultdict

H, W = map(int, input().split())
check_H = defaultdict(int)
check_W = defaultdict(int)

S = [list(input()) for _ in range(H)]

H_max = -1
W_max = -1

for s in range(H):
    tmp = S[s].count("#")
    H_max = max(H_max, tmp)
    check_H[tmp] = s
    
matrix_t = []

for i in range(len(S[0])) :
    tmp = []
    for v in S :
        tmp.append(v[i])
    matrix_t.append(tmp)
    
for i in range(W):
    tmp = matrix_t[i].count("#")
    W_max = max(W_max, tmp)
    check_W[tmp] = i
    
print(check_H[H_max - 1] + 1, check_W[W_max - 1] + 1)