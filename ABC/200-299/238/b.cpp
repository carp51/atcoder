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
ll mod = 998244353;

ll f(ll n) {
    n %= mod;
    return (n * (1 + n) / 2) % mod;
}

ll powll(ll n, ll x) {
    ll tmp = 1;
    for (ll i = 0; i < x; i++){tmp *= n;}
    return tmp;
}

int main() {
    ll N;
    cin >> N;

    string S = to_string(N);
    ll ans = 0;

    for (ll i = 0; i < S.size() - 1; i++)
    {
        ans += f(9 * powll(10, i)) % mod;
    }

    ans += f(N - powll(10, (S.size() - 1)) + 1) % mod;
    
    cout << ans % mod << "\n";
    return 0;
}