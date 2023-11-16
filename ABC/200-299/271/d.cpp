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

void rec(const vector<vector<bool>> &dp, const vector<int> &a, int i, int j, deque<int> &keiro, vector<deque<int>> &ans) {
    if (i == 0) {
        if (j == 0) {
            ans.push_back(keiro);
        }
        return;
    }

    // 上へ遡る (dp[i-1][j] == 0) だったら無視)
    if (dp[i-1][j]) {
        rec(dp, a, i-1, j, keiro, ans);
    }
    // 左上へ遡る (dp[i-1][j-a[i-1]] == 0 だったら無視)
    if (j-a[i-1] >= 0 && dp[i-1][j-a[i-1]]) {
        keiro.push_front(a[i-1]);
        rec(dp, a, i-1, j-a[i-1], keiro, ans);
        keiro.pop_front();
    }
}

int main() {
    int N, S;
    cin >> N >> S;

    vector<string> checkans(N, "H");
    
    int sum = 0;

    vi num;

    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;

        if (a > b)
        {
            checkans[i] == "T";
        }
        

        sum += min(a, b);
        num.push_back(max(a, b) - min(a, b));
    }

    S -= sum;

    int K = S;

    vector<vector<bool>> dp(N + 1, vector<bool>(K + 1, false));

    for (int i = 0; i <= N; i++) {
        dp[i][0] = true;
    }
    // 更新


    for (int i = 0; i < N; i++) {
        for (int k = 0; k <= K; k++) {
            if (k - num[i] >= 0) dp[i + 1][k] = dp[i + 1][k] | dp[i][k - num[i]];
            dp[i + 1][k] = dp[i + 1][k] | dp[i][k];
        }
    }

    if (dp[N][K] == false) {
        cout << "No" << endl;
        exit(0);}
    
    deque<int> keiro;
    vector<deque<int>> ans;
    rec(dp, num, N, K, keiro, ans);

    map<int, int> dic;

    for (int i = 0; i < num.size(); i++)
    {
        dic[num[i]] = i;
    }
    

    while (ans[0].size() > 0)
    {
        if (/* condition */)
        {
            /* code */
        }
        
        checkans[dic[ans[0].front()]] = "T";
        ans[0].pop_front();
    }


    cout << "Yes" << "\n";

    for (int i = 0; i < N; i++) {
       cout << checkans[i];
       if (i < N)cout << "";
       else cout << endl;
       }
    
    return 0;
}