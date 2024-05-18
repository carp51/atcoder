from sortedcontainers import SortedSet, SortedList, SortedDict

'''
S = SortedSet([3, 1, 2])
#SortedSet([1, 2, 3]), 初期化の計算量は O(N * logN)
S.add(4)
#SortedSet([1, 2, 3, 4]), add の計算量は O(logN)
S.add(3)
#SortedSet([1, 2, 3, 4]), 要素は重複しない
S.discard(4)
#SortedSet([1, 2, 3]), 値4を削除 計算量は O(logN) 存在しない要素をdiscardすると、何も起こらない
#S.remove(100) とやると、KeyErrorが出る
S.pop(2)
#S[2]を削除 S.pop()で最大要素の削除 S.pop(0) で最小要素の削除　全部 O(logN)
S[1]
#2 getは O(logN)
S[0:2]
#0 1 スライスなどもできる　これの計算量は長さを k として O(klogN)
len(S)
#2 現在の要素数 O(1)
S.bisect_left(1)
#1
S.bisect_right(1)
#2
#これらは二分探索。 S.bisect_left(x) で、Sにxを挿入する位置(index)を返す。
#S.bisect_right(x) との違いは、すでにxがSにあるときに左に入れるか右に入れるか
#Pythonのbisectと同じ使用感
S.index(2)
#1 Sに2が現れる最初の位置を返す。ないとValueError
S.irange(0,2)
#[1, 2] S に含まれる 0以上2以下（両端含む）の要素を列挙
'''
S = SortedList()
N = int(input())
AC = []
for i in range(N):
    A, C = map(int, input().split())
    AC.append([A, C, i])
    
AC.sort()

for i in range(N):
    S.add(AC[i][1])
    
check = [] 
    
for i in range(N):
    A, C = AC[i][0], AC[i][1]
    S.discard(C)
    
    index = S.bisect_right(C)
    if index != 0:
        check.append(AC[i][2])
        
print(N - len(check))
ans = []
for i in range(N):
    if not i in check:
        ans.append(i + 1)
        
print(*ans)