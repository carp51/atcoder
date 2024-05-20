N, K, P = map(int, input().split())
C = []
A = []

inf = 10 ** 20

# 入力の読み取り
for i in range(N):
    inputs = list(map(int, input().split()))
    C.append(inputs[0])
    A.append(inputs[1:])

# dp配列の初期化
dp = [inf] * ((P + 1) ** K)
dp[0] = 0

# 各提案を順番に処理
for i in range(N):
    cost = C[i]
    improvement = A[i]

    # dp配列のコピーを作成（逆順に更新するため）
    new_dp = dp[:]

    for j in range((P + 1) ** K):
        if dp[j] == inf:
            continue

        # 現在のパラメータの状態を取得
        state = []
        temp = j
        for _ in range(K):
            state.append(temp % (P + 1))
            temp //= (P + 1)

        # 新しいパラメータの状態を計算
        new_state = []
        for k in range(K):
            new_state.append(min(P, state[k] + improvement[k]))

        # 新しい状態を整数に変換
        new_index = 0
        for k in reversed(range(K)):
            new_index = new_index * (P + 1) + new_state[k]

        # 新しい状態のコストを更新
        new_dp[new_index] = min(new_dp[new_index], dp[j] + cost)

    dp = new_dp

# 最終的な目標の状態を整数に変換
goal = (P + 1) ** K - 1

# 結果を出力
result = dp[goal]
print(result if result != inf else -1)
