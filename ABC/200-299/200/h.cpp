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

using namespace std;

using ll = long long;

int main() {
    int t;
    cin >> t;
    while (t--) {
        ll n;
        cin >> n;
        
        ll p = 2, q = 2;
        for (ll i = 2; i * i * i <= n; i++) {
            if (n % i != 0) continue;
            if ((n / i) % i == 0) {
                p = i;
                q = n / i / i;
            } else {
                q = i;
                p = (ll) sqrt(n / i);
            }
            break;
        }
        cout << p << ' ' << q << endl;
    }
}
