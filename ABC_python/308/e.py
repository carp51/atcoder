N = int(input())
A = list(map(int, input().split()))
S = input()

# 動的計画法のテーブルを作成
dp_M = [0] * (N + 1)
dp_ME = [0] * (N + 1)
dp_MEX = [0] * (N + 1)

# テーブルを埋める
for i in range(1, N + 1):
    dp_M[i] = dp_M[i - 1] + (S[i - 1] == 'M')
    
    if S[i - 1] == 'E':
        dp_ME[i] = dp_ME[i - 1] + dp_M[i - 1]
    else:
        dp_ME[i] = dp_ME[i - 1]
        
    if S[i - 1] == 'x':
        dp_MEX[i] = dp_MEX[i - 1] + dp_ME[i - 1]
    else:
        dp_MEX[i] = dp_MEX[i - 1]

# 最終結果を計算
result = 0
for k in range(1, N + 1):
    if S[k - 1] == 'x':
        mex = 0
        if A[k - 1] != 0:
            mex += dp_ME[k - 1]
        if A[k - 1] != 1:
            mex += dp_M[k - 1] * (dp_ME[k - 1] - dp_M[k - 1])
        if A[k - 1] != 2:
            mex += dp_M[k - 1] * dp_M[k - 1] * (dp_ME[k - 1] - dp_M[k - 1])
        result += mex

# 結果を出力
print(result)
