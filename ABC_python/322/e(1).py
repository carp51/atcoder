import numpy as np


#n_ary(変換したい数字, 変換元の基数, 変換後の基数)
#numpyはpypyではなくpythonで提出すること
def n_ary(base, n, m):
    base = str(base)
    decimal_number = int(base, n)
    result_num = np.base_repr(decimal_number, m)
    
    return result_num

def next_Transition(base, diff):
    base = base.rjust(K, "0")
    base = list(map(int, base))
    for i in range(K):
        base[i] += diff[i]
        base[i] = min(P, base[i])
        
    return int(n_ary("".join(map(str, base)), P + 1, 10))


N, K, P = map(int, input().split())
inf = 10 ** 20

dp = [[inf] * ((P + 1) ** K + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(N):
    CA = list(map(int, input().split()))
    C, A = CA[0], CA[1:]
    A_str = "".join(map(str, A))
    for j in range((P + 1) ** K + 1):
        if dp[i][j] != inf:
            next_transition = next_Transition(n_ary(j, 10, P + 1), A)
            dp[i + 1][next_transition] = min(dp[i][j] + C, dp[i + 1][next_transition])
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])

print(dp[-1][-2] if dp[-1][-2] != inf else -1)