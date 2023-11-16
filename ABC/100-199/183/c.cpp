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
    int N, K;
    cin >> N >> K;
    vector<vector<int>> T(N, vector<int>(N));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> T[i][j];
        }
    }

    int ans = 0;

    int j = N - 1;
    vector<int> v(j);
    iota(v.begin(), v.end(), 1);       // v に 1, 2, ... N を設定
    do {
        vi check;
        check.push_back(0);
        for (int i = 0; i < v.size(); i++)
        {
            check.push_back(v[i]);
        }
        check.push_back(0);
        

        int tmp = 0;
        for (int i = 0; i < N; i++)
        {
            tmp += T[check[i + 1]][check[i]];
        }

        if (tmp == K)
        {
            ans += 1;
        }
    } while( next_permutation(v.begin(), v.end()) );     // 次の順列を生成

    cout << ans << "\n";

    return 0;
}