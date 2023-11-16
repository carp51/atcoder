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
    int N, X, Y;
    cin >> N >> X >> Y;

    vector<vector<ll>> dp(2, vector<ll>(N + 1));
    dp[0][1] = 1;

    for (int j = 1; j < N; j++)
    {
        dp[0][j + 1] += dp[0][j];
        dp[1][j] += dp[0][j] * X;
        dp[0][j + 1] += dp[1][j];
        dp[1][j + 1] += dp[1][j] * Y;
    }
    
    cout << dp[1][N] << "\n";
    return 0;
}