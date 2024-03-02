from collections import defaultdict

H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]

S_r = [list(x) for x in zip(*S)]
T_r = [list(x) for x in zip(*T)]

S_check = defaultdict(int)
T_check = defaultdict(int)

for i in range(W):
    tmp_S = "".join(S_r[i])
    tmp_T = "".join(T_r[i])

    S_check[tmp_S] += 1
    T_check[tmp_T] += 1

print("Yes" if T_check == S_check else "No")