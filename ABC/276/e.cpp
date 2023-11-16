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

const int MOD = 998244353;

int main() {
    int Q;
    cin >> Q;

    stack<int> S;
    int n = 1;
    int cnt = 1;
    S.push(1);

    for (int i = 0; i < Q; i++) {
        int q, x;
        cin >> q;
        if (q == 1) {
            cin >> x;
            S.push(x);
            n = 10 * n + x;
            cnt++;
        } else if (q == 2) {
            int tmp = S.top();
            S.pop();
            n -= tmp * pow(10, cnt - 1);
            cnt--;
        } else if (q == 3) {
            int ans = n % MOD;
            cout << ans << endl;
        }
    }
    
    return 0;
}