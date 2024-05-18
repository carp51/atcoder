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
S = SortedSet([3, 1, 2])
N = int(input())

S = SortedList()

for i in range(N):
    A, B = map(int, input().split())
    S.add([A, B])
    
cnt = 0
    
while True:
    flag = True
    cnt += 1
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            S.pop(i + 1)
            S.pop(i)
            flag = False
            break
        
    if not flag:
        continue
        
    for i in range(len(S) - 1):
        if S[i][0] == S[i + 1][0]:
            S.pop(i + 1)
            S.pop(i)
            flag = False
            break
        
    if not flag:
        continue
    
    tmp_S = SortedList()
    
    for i in range(len(S) - 1):
        tmp = S.pop(0)
        tmp_S.add([tmp[1], tmp[0]])
        
    S = tmp_S
    
    for i in range(len(S) - 1):
        if S[i][0] == S[i + 1][0]:
            S.pop(i + 1)
            S.pop(i)
            flag = False
            break
        
    if not flag:
        continue
        
    if flag:
        if cnt % 2 == 0:
            print("Takahashi")
        else:
            print("Aoki")
            
        break