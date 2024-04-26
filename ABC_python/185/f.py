from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

def op(ele1, ele2):
    return ele1 ^ ele2

# SegTree(関数, 単位元, 元となるリスト)
st = SegTree(op, 0, A)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        x -= 1
        st.set(x, st.get(x) ^ y)
    elif t == 2:
        l, r = x - 1, y
        ans = st.prod(l, r)
        print(ans)
        
'''
https://github.com/not522/ac-library-python/blob/master/atcoder/segtree.py
get(i: int) -> T: インデックス i の要素を取得します。セグメント木内
の特定の要素を取得する際に使用します。例えば、与えられたインデックスの
要素を取得する場合に get メソッドを呼び出します。
set メソッド:

set(i: int, x: T) -> None: インデックス i の要素を値 x に更新します。
セグメント木内の要素を変更する際に使用します。例えば、与えられたインデ
ックスの要素を新しい値に更新する場合に set メソッドを呼び出します。

prod メソッド:
prod(l: int, r: int) -> T: インデックス l から r-1 までの範囲の要素
の積（または和、最小値、最大値など、指定した演算）を返します。セグメント
木内の要素の積を求める際に使用します。例えば、区間 [l, r) の要素の積を求
める場合に prod メソッドを呼び出します。

区間 [l, r)なので、lだけ-1する
'''
        