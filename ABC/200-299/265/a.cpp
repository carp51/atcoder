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
    int X, Y, N;
    cin >> X >> Y >> N;

    if (3 * X <= Y)
    {
        cout << X * N << "\n";
    } else
    {
        int ans = Y * (N / 3) + X * (N % 3);
        cout << ans << "\n";
    }
        
    return 0;
}