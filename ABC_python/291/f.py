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

N,M=map(int, input().split())
Uni=UnionFind(N)

for i in range(M):
    A,B=map(int, input().split())
    A-=1
    B-=1
    if Uni.same(A, B):
        print("I")
        exit()
    Uni.merge(A,B)

friends_group=Uni.groups()

friends_size=[]
for fri in friends_group:
    friends_size.append(len(fri))

print(friends_group)
        