class UnionFind:
    def __init__(self, n):
        self.n=n
        self.parent_size=[-1]*n
    #merge(a, b)： a, b を 同じ グループ として 記録
    def merge(self, a, b):
        x, y=self.leader(a), self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
        self.parent_size[x] += self.parent_size[y] 
        self.parent_size[y]=x
        return 
    #同じグループに属するか判定
    def same(self, a, b):
        return self.leader(a) == self.leader(b)
    #a の リーダー を 返す。 a 自身 が リーダー なら a を 返す。 
    def leader(self, a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    #木のサイズを計算
    def size(self, a):
        return abs(self.parent_size[self.leader(a)])
    #全て の グループ を 二次元 配列 の 形 で 返す。 
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


N, M = map(int, input().split())

connect = [[] for _ in range(N + 1)]
Uni=UnionFind(N)

for i in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)
    A-=1
    B-=1
    if Uni.same(A, B):
        print("No")
        exit(0)
    Uni.merge(A,B)

one_count, two_count = 0, 0

for i in range(1, N + 1):
    if len(connect[i]) == 1:
        one_count += 1
    elif len(connect[i]) == 2:
        two_count += 1
    else:
        print("No")
        exit(0)

print("Yes")