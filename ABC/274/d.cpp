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

bool partial_sum(vi a, int K) {
    int N = a.size();
    K = abs(K);
    // 二次元配列
    vector<vector<bool>> dp(N + 1, vector<bool>(K + 1, false));
    // 初期化
    for (int i = 0; i <= N; i++) {
        dp[i][0] = true;
    }
    // 更新
    for (int i = 0; i < N; i++) {
        for (int k = 0; k <= K; k++) {
            if (k - a[i] >= 0) dp[i + 1][k] = dp[i + 1][k] | dp[i][k - a[i]];
            dp[i + 1][k] = dp[i + 1][k] | dp[i][k];
        }
    }
    if (dp[N][K]) {
        return true;
    } else {
        return false;
    }
}

int main() {
    int N, x, y;
    cin >> N >> x >> y;

    vi o_v;
    vi e_v;

    vector<int> A(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    for(int i = 0; i < N; i++) {
        if (i % 2 != 0)
        {
            o_v.push_back(A[i]);
        } else {
            e_v.push_back(A[i]);
        }
    }

    int sum_o = accumulate(o_v.begin(), o_v.end(), 0);
    int sum_e = accumulate(e_v.begin(), e_v.end(), 0);

    for (int i = 0; i < o_v.size(); i++)
    {
        o_v[i] = 2 * o_v[i];
    }
    
    for (int i = 0; i < e_v.size(); i++)
    {
        e_v[i] = 2 * e_v[i];
    }

    e_v[0] = 0;

    if (partial_sum(o_v, sum_o - y) and partial_sum(e_v, sum_e - x))
    {
        cout << "Yes" << "\n";
    } else
    {
        cout << "No" << "\n";
    }
    
    

    return 0;
}