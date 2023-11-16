class UnionFind:
    def __init__(self, n):
        self.n=n
        self.parent_size=[-1]*n
    def merge(self, a, b):
        x, y=self.leader(a), self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
        self.parent_size[x] += self.parent_size[y] 
        self.parent_size[y]=x
        return 
    def same(self, a, b):
        return self.leader(a) == self.leader(b)
    def leader(self, a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    def size(self, a):
        return abs(self.parent_size[self.leader(a)])
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

N = int(input())

from collections import defaultdict
    
check = defaultdict(int)

now_n = 1

tmp = []

for i in range(N):
    S, T = map(str, input().split())

    s, t = 0, 0

    if check[S] != 0:
        s = check[S]
    else:
        check[S] = now_n
        now_n += 1
        s = check[S]

    if check[T] != 0:
        t = check[T]
    else:
        check[T] = now_n
        now_n += 1
        t = check[T]

    tmp.append([s, t])

Uni=UnionFind(len(check) + 100)

for i in range(N):
    s, t = tmp[i][0], tmp[i][1]
    s -= 1
    t -= 1
    if Uni.same(s,t):
        print("No")
        exit()
    Uni.merge(s, t)

print("Yes")
