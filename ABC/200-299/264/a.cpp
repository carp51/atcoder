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
    int L, R;
    cin >> L >> R;

    string S = "atcoder";

    for (int i = L - 1; i < R; i++) {
       cout << S[i];
    }
    return 0;
}