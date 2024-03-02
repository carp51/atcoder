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
    ll N, M;
    cin >> N >> M;
    vector<ll> A(N);
    for(ll i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    vector<ll> csA(N + 1);
    csA[0] = 0;
    for (ll i = 0; i < N; i++)
        csA[i + 1] = csA[i] + A[i];
    
    int n_sum = 0;

    for (int i = 0; i < M; i++)
    {
        n_sum += (i + 1) * A[i];
    }

    int ans = n_sum;

    for (int i = 0; i < N - M; i++)
    {
        n_sum -= A[i];
        n_sum -= csA[i + M] - csA[i + 1];
        n_sum += M * A[i + M];

        ans = max(ans, n_sum);
    }

    cout << ans << "\n";
    
    return 0;
}