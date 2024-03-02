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

    vvi dp(24);
    dp[0] = {1};

    for (int i = 1; i < N; i++)
    {
        for (int j = 0; j < dp[i - 1].size(); j++)
        {
            dp[i].push_back(dp[i - 1][j]);
        }

        dp[i].push_back(i + 1);

        for (int j = 0; j < dp[i - 1].size(); j++)
        {
            dp[i].push_back(dp[i - 1][j]);
        }
        
    }

    for (int i = 0; i < dp[N - 1].size(); i++) {
        cout << dp[N - 1][i];
        if (i < dp[N - 1].size())cout << " ";
        else cout << endl;
    }
    
    return 0;
}