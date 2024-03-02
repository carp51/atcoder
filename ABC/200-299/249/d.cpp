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

    vvi dp;
    dp.push_back({1});

    for (int i = 0; i < N - 1; i++)
    {
        vi tmp;
        for (int j = 0; j < dp.back().size(); j++){tmp.push_back(dp.back()[j]);}
        tmp.push_back(i + 2);
        for (int j = 0; j < dp.back().size(); j++){tmp.push_back(dp.back()[j]);}

        dp.push_back(tmp);
    }

    vi ans = dp.back();

    for (int i = 0; i < ans.size(); i++) {
       cout << ans[i];
       if (i < ans.size())cout << " ";
       else cout << endl;
       }
    
    return 0;
}