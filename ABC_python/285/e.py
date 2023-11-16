# 頂点数:n
# edge[i]:頂点iと辺で結ばれる頂点の集合

n = int(input())
edge = []

from collections import defaultdict
    
check = defaultdict(int)

now_n = 0

for i in range(n):
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

    edge.append((s, t))



# 遷移元の頂点
parent=[-1]*n
# 閉路に含まれる辺の集合
loop =set()
# 既に探索した頂点か
come=[False]*n

def dfs(x,last=-1):
    if last!=-1:
        parent[x]=last
    come[x]=True
    for i in edge[x]:
        if i ==last:continue
        if come[i]:
            now=x
            loop.add((now,i))
            loop.add((i,now))
            while now!=i:
                loop.add((now,parent[now]))
                loop.add((parent[now],now))
                now=parent[now]
            return True
        else:
            if dfs(i,x):
                return True
    return False

print(dfs())