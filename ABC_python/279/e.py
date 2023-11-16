from decimal import Decimal, ROUND_HALF_UP
A, B = map(float, input().split())

#(1)最小にしたい関数fを定義する
def f(x):
    global A, B
    return B * x + (A / (pow(x + 1, 0.5)))

#(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
l,r=0,10**18
#(3)誤差が10^-8を下回るまでwhile文を回す
while l + 0.0001 < r:
    #(4)オーバーフローしないように以下のように三等分点を置く
    c1=l+(r-l)/3
    c2=r-(r-l)/3
    #(5)更新を行う
    if f(c1)<f(c2):
        r=c2
    else:
        l=c1
#(6)最終的に出力するのはl,rのどちらでも良い

b = int(l)

ans = 10 ** 20

for i in range(b - 50, b + 50):
    if i < 0:
        continue
    ans = min(ans, f(i))

print(ans)

