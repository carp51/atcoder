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
N = int(input())
A = list(map(int, input().split()))
S = SortedList(A)

cnt = 0

while S[-1] - S[0] > 1:
    min_num = S.pop(0)
    max_num = S.pop()
    
    if (min_num + max_num) % 2 == 0:
        tmp = (min_num + max_num) // 2
        S.add(tmp)
        S.add(tmp)
        cnt += max_num - tmp
        print(0)
    else:
        tmp = (min_num + max_num) // 2
        S.add(tmp)
        S.add(tmp + 1)
        cnt += tmp - min_num
    
print(S, cnt)