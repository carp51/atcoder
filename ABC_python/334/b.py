def is_ok(arg, flag):
    if flag:
        return A + arg * M >= L
    else:
        return A + arg * M >= R


def meguru_bisect(ng, ok, flag):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, flag):
            ok = mid
        else:
            ng = mid
    return ok

A, M, L, R = map(int, input().split())

l = meguru_bisect(-10 ** 20 - 1, 10 ** 20 + 1, True)
r = meguru_bisect(-10 ** 20 - 1, 10 ** 20 + 1, False)

if (A + r * M) == R:
    r += 1

ans = ((A + (r - 1) * M) - (A + l * M)) // M

print(ans + 1)