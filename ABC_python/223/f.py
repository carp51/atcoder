from atcoder.segtree import SegTree

N, Q = map(int, input().split())
S = list(input())
A = []

cs = [0]

for i in range(N):
    if S[i] == "(":
        A.append(1)
    else:
        A.append(-1)
        
for i in range(N):
    cs.append(cs[-1] + A[i])

def op(ele1, ele2):
    return ele1 + ele2

# SegTree(関数, 単位元, 元となるリスト)
st = SegTree(op, 0, A)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        x -= 1
        y -= 1
        tmp = st.get(x)
        st.set(x, st.get(y))
        st.set(y, tmp)
    elif t == 2:
        l, r = x - 1, y
        ans = st.prod(l, r)
        print(ans)
        
'''
https://github.com/not522/ac-library-python/blob/master/atcoder/segtree.py
get(i: int) -> T: インデックス i の要素を取得します。セグメント木内
の特定の要素を取得する際に使用します。例えば、与えられたインデックスの
要素を取得する場合に get メソッドを呼び出します。

set(i: int, x: T) -> None: インデックス i の要素を値 x に更新します。
セグメント木内の要素を変更する際に使用します。例えば、与えられたインデ
ックスの要素を新しい値に更新する場合に set メソッドを呼び出します。

prod(l: int, r: int) -> T: インデックス l から r-1 までの範囲の要素
の積（または和、最小値、最大値など、指定した演算）を返します。セグメント
木内の要素の積を求める際に使用します。例えば、区間 [l, r) の要素の積を求
める場合に prod メソッドを呼び出します。

区間 [l, r)なので、lだけ-1する

max_right(f: Callable[[Any], bool]) -> int: 与えられた関数 f を使って
セグメント木上で二分探索を行います。この関数は、引数として要素 x を受け取
り、真偽値を返す必要があります。max_right は、条件 f を満たす最大のインデ
ックス r を返します。
'''    