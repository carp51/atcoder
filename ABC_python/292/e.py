from collections import defaultdict
# 深さ優先探索
def dfs(G, v, seen):
    seen[v] = True
    global cnt
    for e in G[v]:
        if not seen[e['to']]:  # 訪問済みでなければ探索
            dfs(G, e['to'], seen)
            cnt += 1

n, m = map(int, input().split())
check = defaultdict(int)

G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a-1].append({'to': b-1})
    G[b-1].append({'to': a-1})
    check[(a - 1, b - 1)] += 1
    check[(b - 1, a - 1)] += 1

seen = [False] * n  # 初期化
cnt = 0
for i in range(n):
    if not seen[i]:
        cnt = 1
        v_cnt = 1
        dfs(G, i, seen)
        
print(cnt)
        
