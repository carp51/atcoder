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

    swap(S[0], S[1]);
    swap(S[1], S[2]);
    cout << S << "\n";
    return 0;
}