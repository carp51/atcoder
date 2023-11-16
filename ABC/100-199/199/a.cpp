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
    int A, B, C;
    cin >> A >> B >> C;

    if (A * A + B * B < C * C)
    {
        cout << "Yes" << "\n";
    } else
    {
        cout << "No" << "\n";
    }

    return 0;
}