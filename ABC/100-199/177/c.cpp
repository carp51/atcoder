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

int main() {
    int N;
    cin >> N;
    vll A(N);
    int mod = 1000000007;
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    vll csA(N + 1);
    csA[0] = 0;
    for (int i = 0; i < N; i++)
        csA[i + 1] = csA[i] + A[i];
    
    ll ans = 0;
    for (int i = 1; i < N; i++)
    {
        ll tmp = 0;
        tmp = (A[i - 1] % mod) * ((csA.back() - csA[i]) % mod);
        ans += tmp % mod;
    }

    cout << ans % mod << "\n";
    
    return 0;
}