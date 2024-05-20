import numpy as np


#n_ary(変換したい数字, 変換元の基数, 変換後の基数)
#numpyはpypyではなくpythonで提出すること
def n_ary(base, n, m):
    base = str(base)
    decimal_number = int(base, n)
    result_num = np.base_repr(decimal_number, m)

    return result_num


N, K, P = map(int, input().split())
C = [0]
A = [0]

inf = 10 ** 20

for i in range(N):
    c, *a = map(str, input().split())
    C.append(int(c))
    tmp = "".join(a)
    A.append(int(n_ary("".join(a), P + 1, 10)))

dp = [[inf] * ((P + 1) ** K) for i in range(N + 1)]

for i in range(N + 1):
    for j in range((P + 1) ** K):
        if i != N   :
            if j == A[i + 1]:
                dp[i + 1][j] = min(dp[i + 1][j], C[i + 1])
                
            flag = True
                
            if dp[i][j] != inf:
                dp[i + 1][j] = min(dp[i][j],  dp[i + 1][j])
                index = j + A[i + 1]
                check = []
                if j + A[i + 1] >= ((P + 1) ** K) - 1:
                    n, m = n_ary(j, 10, P + 1), n_ary(A[i + 1], 10, P + 1)
                    n = n.zfill(max(len(n), len(m)))
                    m = m.zfill(max(len(n), len(m)))
                    
                    for k in range(max(len(n), len(m))):
                        check.append(str(min(P, int(n[k]) + int(m[k]))))
                        if int(n[k]) + int(m[k]) > P:
                            flag = False
                            
                if not flag:
                    index = int(n_ary("".join(check), P + 1, 10))
                          
                dp[i + 1][index] = min(dp[i + 1][index], dp[i][j] + C[i + 1])
                    


print(dp[-1][-1] if dp[-1][-1] != inf else -1)