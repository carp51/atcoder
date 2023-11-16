MOD = 10**9+7  # 余りを求めるための値

# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 各要素を MOD で割った余りを計算し、10^9+7 乗する
sum_A = sum(pow(a, MOD, MOD) for a in A)

# 結果を出力する
print(sum_A % MOD)
