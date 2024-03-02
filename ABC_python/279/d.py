from decimal import *
A, B = map(float, input().split())

min_num = max(B * 0 + (A / ((1) ** 0.5)), B * (10 ** 18 + 100) + (A / ((10 ** 18 + 100) ** 0.5)))

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    return min_num >= B * arg + (A / ((arg + 1) ** 0.5))


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

        global min_num
        min_num = min(B * mid + (A / ((mid + 1) ** 0.5)), min_num)
    return ok

tmp = meguru_bisect(-1, 10 ** 18 + 1)
print(B * tmp + (A / ((tmp + 1) ** 0.5)))