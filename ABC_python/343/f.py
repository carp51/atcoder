from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# SegTree(関数, 単位元, 元となるリスト)
st = SegTree(max, -1, A)

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 1:
        x, v = q
        x -= 1
        st.set(x, v)
    elif t == 2:
        l, r = q
        ans = st.prod(l - 1, r)
        print(ans)
    elif t == 3:
        x, v = q
        x -= 1
        ans = st.max_right(x, lambda el: el < v) + 1
        print(ans)