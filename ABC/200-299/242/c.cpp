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

    ll mod = 998244353;

    vector<vector<ll>> dp(N + 1, vector<ll>(9));
    for(int i = 0; i < N + 1; i++) {
        for(int j = 0; j < 9; j++) {
            dp[i][j] = 0;
        }
    }

    for (int i = 1; i < N + 1; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (i == 1){dp[i][j] = 1;}
            else
            {
                if (j == 0)
                {
                    dp[i][j] = (dp[i - 1][j] % mod + dp[i - 1][j + 1] % mod) % mod;
                } else if (j == 8)
                {
                    dp[i][j] = (dp[i - 1][j] % mod + dp[i - 1][j - 1] % mod) % mod;
                } else
                {
                    dp[i][j] = (dp[i - 1][j + 1] % mod + dp[i - 1][j] % mod + dp[i - 1][j - 1] % mod) % mod;
                }
            }
            
        }
        
    }

    ll ans = 0;

    for (ll i = 0; i < 9; i++)
    {
        ans += dp.back()[i] % mod;
    }
    
    cout << ans % mod << "\n";

    return 0;
}