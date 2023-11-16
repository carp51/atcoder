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

bool is_ok(string arg, ll A, ll B, ll X) {
    return A * stoll(arg) + B * arg.size() <= X;
}

ll meguru_bisect(ll ng,  ll ok, ll A, ll B, ll X) {
    while (abs(ok - ng) > 1)
    {
        ll mid = (ok + ng) / 2;
        if (is_ok(to_string(mid), A, B, X)){ok = mid;}
        else{ng = mid;}   
    }

    return ok;  
}

int main() {
    ll A, B, X;
    cin >> A >> B >> X;

    ll ans = meguru_bisect(pow(10, 9) + 1, 0, A, B, X);

    cout << ans << "\n";
    
    return 0;
}