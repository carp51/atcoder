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
    string S;
    cin >> S;
    int N = S.size();
    vector<char> v(N);
    for (int i = 0; i < N; i++)
    {
        v[i] = S[i];
    }    // v に 1, 2, ... N を設定
    do {
        for(auto x : v) cout << x << " "; cout << "\n";    // v の要素を表示
    } while( next_permutation(v.begin(), v.end()) );     // 次の順列を生成
    
    return 0;
}