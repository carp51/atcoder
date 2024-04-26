# これはfindで再起を使っているから．
import sys
sys.setrecursionlimit(10**6)

class UnionFind:
  
  def __init__(self, n):
    self.Null = "nullNullUnagi"
    self.n = n
    self.groupCount = n
    # それぞれの根っこ(親)を表す．
    # もし，自分が根っこならば，-(子供の数)が入っている．
    self.parents = [-1] * n
    
  # xの根っこを返す
  def find(self, x):
    # ルートならば
    if self.parents[x] < 0:
      return x
    # 子供ならば(parents[x]が親を指すなら)
    else:
      # 経路圧縮
      self.parents[x] = self.find(self.parents[x]) # 親の親を親とする．
      return self.parents[x]
  
  # xとyを合併する．
  def union(self, x, y):
    xRoot = self.find(x)
    yRoot = self.find(y)
    
    # 根っこが一緒ならば既に併合されている
    if(xRoot == yRoot):
      return
    else:
      self.groupCount -= 1
 
    # Union by Rank
    # 根っこの親は自分の子供の数を表現している．
    if(self.parents[xRoot] < self.parents[yRoot]):
      # なるべく左側を親にする
      xRoot, yRoot = yRoot, xRoot
      
    self.parents[xRoot] += self.parents[yRoot] # 左のノードの子供の数を増やす．
    self.parents[yRoot] = xRoot # 右のノードの親をyRootとして登録する．
    
  # xと同じメンバーの数
  def size(self, x):
    return -self.parents[self.find(x)]
    
  # xとyが同じメンバーか
  def same(self, x, y):
    return self.find(x) == self.find(y)
    
  # xと同じメンバーを返す．
  def members(self, x):
    root = self.find(x) # root処理を一回で済ませるため
    return [i for i in range(self.n) if self.find(i) == root]
      
  # rootメンバーを返す
  def roots(self):
    return [i for i in range(self.n) if self.parents[i] < 0 ]


N, M = map(int, input().split())

uf = UnionFind(N)

for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1

  uf.union(a, b)
  
ans = 0

for r in uf.roots():
    ans += uf.size(r) * (uf.size(r) - 1) // 2
    
print(ans - M)