from collections import defaultdict


def f(x):
    if x == 1:
        return 0
    return x * (x - 1) // 2


#2部グラフならTrue, そうでなければFalse
def is_bipartite():
    stack = [(start,1)] # (頂点、色)のタプルをスタックする。最初は(頂点0, 黒(1))
    while stack:
        #スタックから最後に追加された(頂点, 色)をpop
        v,color = stack.pop()
        #今いる点を着色
        colors[v] = color
        #今の頂点から行けるところをチェック
        for to in connect[v]:
            #同じ色が隣接してしまったらFalse
            if colors[to] == color:
                 return False
            #未着色の頂点があったら反転した色と共にスタックに積む
            if colors[to] == 0:
                if color == -1:
                    U[to] = -1
                else:
                    V[to] = -1
                stack.append((to, -color))
    #調べ終わったら矛盾がないのでTrue
    return True

N, M = map(int, input().split())

check = defaultdict(list)

U, V = defaultdict(int), defaultdict(int)

connect = [[] for _ in range(N + 10)]

start = -1

for i in range(M):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

    start = u

colors = [0 for i in range(N + 10)]

if not is_bipartite():
    print(0)
    exit()

U[start] = -1

u_l = []
v_l = []

for i in range(1, N + 1):
    if U[i] == -1:
        u_l.append(i)
    
    if V[i] == -1:
        v_l.append(i)


ans = f(N) - f (len(u_l)) - f(len(v_l)) - M

print(ans)