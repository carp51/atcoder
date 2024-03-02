def is_ok(arg):
    return i * arg >= M


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


N, M = map(int, input().split())

ans = 10 ** 20

for i in range(1, int(M ** 0.5) + 100):
    if i > N:
        break
    tmp = i * meguru_bisect(0, N)
    if tmp < M:
        continue
    ans = min(ans, tmp)
    
if ans == 10 ** 20:
    ans = -1

print(ans)