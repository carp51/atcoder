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

int main()
{
    int N;
    cin >> N;
    vector<pair<int, int>> LR(N);
    for (int i = 0; i < N; i++)
    {
        cin >> LR[i].first >> LR[i].second;
    }
    // cout << check[1].second << "\n";

    sort(LR.begin(), LR.end());

    vvi ans = {{-10, -10}};

    for (int i = 0; i < N; i++)
    {
        if (ans.back()[1] < LR[i].first)
        {
            ans.push_back({LR[i].first, LR[i].second});
        }
        else
        {
            ans.back()[1] = max(ans.back()[1], LR[i].second);
        }
    }

    for (int i = 1; i < ans.size(); i++)
    {
        cout << ans[i][0] << " " << ans[i][1] << "\n";
    }

    return 0;
}