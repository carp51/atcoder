#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;
using ll = long long;
using vi = vector<ll>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvl = vector<vl>;
using vvll = vector<vll>;
using vs = vector<string>;
using pii = pair<ll, ll>;

int main() {
    ll N, M;
    cin >> N >> M;
    vector<ll> A(N);
    for(ll i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    vector<vector<ll>> dp(M + 1, vector<ll>(N + 1));
    for(ll i = 0; i < M + 1; i++) {
        for(ll j = 0; j < N; j++) {
            dp[i][j] = -5000000000000;
        }
    }

    for (ll i = 1; i < N + 1; i++)
    {
        dp[1][i] = max(dp[1][i - 1], A[i - 1]);
    }
    
    for (ll i = 2; i < M + 1; i++)
    {
        for (ll j = i; j < N + 1; j++)
        {
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + i * A[j - 1]);
        }
        
    }
    
    cout << dp[M][N] << "\n";
    return 0;
}