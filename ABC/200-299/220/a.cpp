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

    for (int i = 1; i < 100000; i++)
    {
        if (A <= C * i and C * i <= B)
        {
            cout << C * i << "\n";
            exit(0);
        }
    }
    
    cout << -1 << "\n";
    return 0;
}