p = 34

def f(x):
    global p
    return p * x ** 2 + x + 12

#(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
l,r=0,10**18
#(3)誤差が10^-8を下回るまでwhile文を回す
while l + pow(10, -8) < r:
    #(4)オーバーフローしないように以下のように三等分点を置く
    c1=l+(r-l)/3
    c2=r-(r-l)/3
    #(5)更新を行う
    if f(c1)<f(c2):
        r=c2
    else:
        l=c1
#(6)最終的に出力するのはl,rのどちらでも良い

print(f(l))