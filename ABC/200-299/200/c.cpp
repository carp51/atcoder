#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvl = vector<vl>;
using vvll = vector<vll>;
using vs = vector<string>;
using pii = pair<int, int>;

ll f(ll  n) {
    return n * (n - 1) / 2;
}

int main() {
    int N;
    cin >> N;
    vector<ll> A(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    map<ll, int> dic;
    for (int i = 0; i < N; i++){dic[A[i] % 200] = 0;}
    for (int i = 0; i < N; i++){dic[A[i] % 200] += 1;}

    ll ans = 0;

    for(auto i = dic.begin(); i != dic.end(); ++i){
            ll v = i->second;

            ans += f(v);  
    }

    cout << ans << "\n";
    return 0;
}