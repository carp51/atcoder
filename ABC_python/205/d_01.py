from bisect import bisect_right

def is_ok(arg):
    return arg - bisect_right(A, arg) >= K


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
    return ok


N, Q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(Q):
    K = int(input())
    
    print(meguru_bisect(0, 10 ** 20 + 1))