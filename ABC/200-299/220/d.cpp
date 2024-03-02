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
    vector<int> A(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }   

    vector<vector<ll>> dp(N, vector<ll>(10));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < 10; j++) {
            dp[i][j] = 0;;
        }
    }

    dp[0][A[0]] = 1;
    
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (dp[i][j] != 0)
            {
                dp[i + 1][(j + A[i + 1]) % 10] += dp[i][j] % mod;
                dp[i + 1][(j * A[i + 1]) % 10] += dp[i][j] % mod;
            } 
        }  
    }
    
    for (int i = 0; i < 10; i++) {
       cout << dp.back()[i] % mod << endl;
    }
    return 0;
}