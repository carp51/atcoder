import sys

n = int(input())

# 1回目のクエリでS[1]を得る
print("? 1")
sys.stdout.flush()
s1 = int(input())

# 2回目のクエリでS[N]を得る
print("? {}".format(n))
sys.stdout.flush()
sn = int(input())

# S[1]とS[N]が同じ場合は、Sの中に01が存在することになるため、S[2]を取得する
if s1 == sn:
    left, right = 1, n
    while right - left > 1:
        mid = (left + right) // 2
        print("? {}".format(mid))
        sys.stdout.flush()
        x = int(input())
        if x == s1:
            left = mid
        else:
            right = mid
    print("! {}".format(right))
else:
    # S[1]とS[N]が異なる場合は、単調増加もしくは単調減少する箇所を探す
    left, right = 1, n
    while right - left > 1:
        mid = (left + right) // 2
        print("? {}".format(mid))
        sys.stdout.flush()
        x = int(input())
        if x == s1:
            left = mid
        else:
            right = mid
    if s1 == 0:
        print("! {}".format(left))
    else:
        print("! {}".format(right))
sys.stdout.flush()
