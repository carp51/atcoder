def solve(N, dishes):
    dishes = [(x, y) for x, y in sorted(enumerate(dishes), key=lambda x: -x[1][1])]
    dp = [[float('-inf') for _ in range(N+2)] for _ in range(N+2)]
    dp[0][0] = 0

    for i in range(N):
        idx, (X, Y) = dishes[i]
        for j in range(i+1):
            if dp[i][j] != float('-inf'):
                # 解毒剤入り料理を食べる選択肢（いつでも食べられる）
                if X == 0:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j] + Y)
                # 毒入り料理を食べる選択肢（ただし、お腹を壊していない時のみ）
                elif X == 1 and j < i+1:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + Y)
                # 料理を食べない選択肢
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])

    return max(dp[N])

# 入力例
N = int(input())
dishes = [list(map(int, input().split())) for _ in range(N)]
print(solve(N, dishes))  # 出力例: 90
